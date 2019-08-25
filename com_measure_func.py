# coding: utf-8
# pymongo 2.5 sample
#
import pymongo
from datetime import datetime
import pandas as pd
import numpy as np
#
class ComMeasureFunc:
    """ mongoDb class
    """
    #HOST = "1234"
    
    ###########################
    #
    ###########################
    def __init__(self):
        self.aa =0
    ###########################
    #
    ###########################
    def conver_xAxis(self, items ):
        arr = []
        for item in items:
#            print( type(item["mdate"]) )
#            print( item["mdate"] )
            arr.append( item["mdate"] )
        print("# conver_xAxis")
        return arr
    ###########################
    #
    ###########################
    def conver_hnum(self, items ):
        arr = []
        for item in items:
            arr.append( item["hnum"] )
        return arr



