#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:59:03 2019

@author: shriganeshkolhe
"""


import pandas as pd
import os

mydir = "/Users/shriganeshkolhe/Desktop/RA/Python_scripts/indiazipcode/indiazipcode/"
os.chdir(mydir)
filelist = []

zipfile = "dataset/all_india_zipcode.csv"
csv_input = pd.read_csv(mydir + zipfile, encoding ='latin1',  sep=',', \
                            engine='python', quotechar = '"', skipinitialspace=True )

#set_simple_zipcode = True
#
#def SearchEngine(self,in_bool):
#    self.simple_zipcode = in_bool
#    pass
#
     
class by_zipcode:
    def __init__(self, zipcode):
        self.zipcode = int(str(zipcode).strip())
    
    def is_valid(self):
        if self.zipcode in csv_input['pincode'].tolist(): 
            return True
        else:
            return False
        
    def values(self):       
        csv_input.set_index('officename', inplace=True)
        mask = csv_input.loc[csv_input['pincode'] == self.zipcode ]
        return (mask)
    
    def to_json(self):
        return(self.values().to_json())
    
    def to_dict(self):
        return(self.values().to_dict())
        

#print(j.is_valid())
        
##useful resources##
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/