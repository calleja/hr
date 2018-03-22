#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 00:13:29 2018

@author: lechuza
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('/home/lechuza/Documents/hr/Flatiron_Analyst_Case_Study_(2).xlsx')

df.dtypes
df.head()
for i in np.arange(0,df.shape[1]):
    print(df.iloc[:,i].value_counts())
    
''' 
'month of service' is nearly qualitative    
'Denied Amount' is continuous for all intents and purposes
'Insurance Name' is categorical
'Service Line' is Categorical
'Denial Type' is Categorical '''

#splitting dataset into first and second half of year
first_half=df.loc[df['Month of Service'] <7,:]
second_half=df.loc[df['Month of Service'] >6,:]

#create dataframe of frequencies of the variables I want to plot
#will need to sort the series by index - alphabetical order
dt_1=first_half['Denial Type'].value_counts()
print(dt_1.values)
dt_1.index
dt_2=second_half['Denial Type'].value_counts()
dt_2.index

#plot denial types for first and second half of year

plt.subplot(2,1,1)
plt.bar(np.arange(1,len(dt_1)+1),dt_1.values)
plt.subplot(2,1,2)
plt.bar(np.arange(1,len(dt_2)+1),dt_2.values)
plt.show()