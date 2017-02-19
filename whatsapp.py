# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 08:23:56 2017

@author: yossi
"""
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from numpy import math

with open("C:\\Users\\yossi\\Desktop\\_chat111.txt",encoding="utf-8") as file:
    
    data = []
    num = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    
    for line in file:
        temp = line   
        line = line[:-1].split(':')
        #breaking down the date
        first = line[0].split(', ')
        line.remove(line[0])
        hour = [first[-1]]
        #breaking down the time
        if isinstance(line,list)==True and len(line)>=1:
            minute = [line[0]]
            line.remove(line[0])
        if isinstance(line,list)==True and len(line)>=1:
            sec = [line[0]]
            line.remove(line[0])
        date = first[0].split('.')
        line = date+hour+minute+sec+line
        if len(line)>=9:
            line[-2] = line[-2]+":"+line[-1]
            line.remove(line[-1])
            if len(line)==9:
                line[-2] = line[-2]+":"+line[-1]
                line.remove(line[-1])     
        #chars counting
        words = []
        if line[-1]!=" <‏התמונה הושמטה>" and line[-1]!=" <‏קטע קול הושמט>" and line[-1]!=" <‏הסרט הושמט>":
            words.append(len(line[-1].strip(" ")))
        else:
            words.append(0)
        
        line = line+words
        #movies, pictures and voacl messages counting 
        isVoice = []
        isPic = []
        isMovie = []

        if line[-2]==" <‏התמונה הושמטה>":
            isPic.append(1)
        else:
            isPic.append(0)
        if line[-2]==" <‏קטע קול הושמט>":
            isVoice.append(1)
        else:
            isVoice.append(0)
        if line[-2]==" <‏הסרט הושמט>":
            isMovie.append(1)
        else:
            isMovie.append(0)
                
        line = line+isPic+isVoice+isMovie
        #new line use case handeling
        if len(data)> 0 and (len(line)<len(data[-1]) or len(line)>12 or line[1] not in num):
            data[-1][-5] = data[-1][-5]+" "+temp
            data[-1][-4] = len(data[-1][-5].strip(" "))
        else:
            data.append(line)
#creatung the data frame            
pd = pd.DataFrame(data,columns=["day","month","year","hour","minute","second","sender","message","chars","isPic","isVoice","isMovie"])
#
result = pd.groupby(["sender"])["chars"].mean().sort_values(axis=0,ascending=False)

     