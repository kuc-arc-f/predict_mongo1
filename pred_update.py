#sk_iot_2
# encoding: utf-8
# 2019/08/24
# in: measure.csv
# 予測結果を、mongoDBに更新する。
#

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import time
import datetime as dt
from db_mongo_func import dbMongoFunc
from com_measure_func import ComMeasureFunc

#
def conv_tm2float(nDim ):
	ret=[]
	for item in nDim:
		ret.append(item.total_seconds())
	return ret

###########################
# main
###########################
db = dbMongoFunc()
d= db.get_measureDat()
#print(d)
f = ComMeasureFunc()
arr_X = f.conver_xAxis(d)
arr_Y = f.conver_hnum(d)
#print(arr_Y )
arr = {'time': arr_X
        ,'hnum': arr_Y
}
rdDim = pd.DataFrame(arr )
#print(rdDim.head(10 ) )

rdDim.info()
#rdDim.describe()
#quit()

# Y
Y = rdDim["hnum"]
Y = np.array(Y, dtype = np.float32).reshape(len(Y) ,1)
# X
#xDim =np.arange(len(Y ))
xAxis= np.array(rdDim['time']).reshape(len(rdDim['time'] ) ,1)

min = rdDim['time'].min()
rdDim['diff'] = rdDim['time'] -min
#print(rdDim['diff'][0])
diff = conv_tm2float(rdDim['diff'] )
#print(diff )
xDim =np.array(diff )
print(xDim)
#quit()

X = np.array(xDim, dtype = np.float32).reshape(len(xDim ) ,1)
#quit()

print ("start...")
start_time = time.time()

# 予測モデルを作成
clf = linear_model.LinearRegression()
clf.fit(X, Y)

# 回帰係数
print(clf.coef_)
# 切片 (誤差)
print(clf.intercept_)
# 決定係数
print(clf.score(X, Y))

#predict
pred = clf.predict(X)

interval = int(time.time() - start_time)
print ("実行時間: {}sec".format(interval) )
#quit()

#db
#print(xAxis.shape , pred.shape)
db = dbMongoFunc()
db.insert_pred(arr_X, Y, pred)
