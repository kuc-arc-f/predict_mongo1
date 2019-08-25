# coding: utf-8
# pymongo 2.5 sample
#
import pymongo
from datetime import datetime
import pandas as pd
import numpy as np
#
class dbMongoFunc:
    """ mongoDb class
    """
    #HOST = "1234"

    ###########################
    #
    ###########################
    def __init__(self):
        client = pymongo.MongoClient(host='192.168.10.104', port=27017)
        self.db = client.app1db
    ###########################
    #
    ###########################
    def insert_pred(self, xAxis, Y, pred):
        print("# insert_pred")
#        xArr = []
        i = 0
        for item in xAxis:
            print( xAxis[i] )
            data = {
                'mdate': xAxis[i],
                'pred' : float(pred[i]),
                'hnum': float(Y[i]),
                'up_date': datetime.now()
            }
            self.db.pred.save(data)
            i += 1
#            xArr.append(item)
        print(len(xAxis) )
    ###########################
    #
    ###########################
    def get_measureDat(self ):
        ret = None
        # find
        items = []
        cursor = self.db.dats.find()
        for item in cursor:
        #    print(post["title"] )
#            print(item )
            items.append(item)
        ret = items
        return ret


