# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:38:12 2021

@author: apurb
"""

import pandas as pd
df=pd.read_csv("sec_bhavdata_full_01102021.csv",skipinitialspace=(True))
df.replace("-","",inplace=True)
df["CHANGE"]=df["CLOSE_PRICE"]-df["PREV_CLOSE"]
df["DELIV_PER"]=pd.to_numeric(df["DELIV_PER"])
data=df["SYMBOL"][(df.SERIES=="EQ")&(df.DELIV_PER>=50)&(df["CHANGE"]>0)]
ndf=pd.DataFrame(data)  #to save into new dataframe
ndf.to_csv("APURBA.csv")   #to save into apurba.csv file
print(data)