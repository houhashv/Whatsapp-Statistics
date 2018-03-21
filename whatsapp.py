# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 20:40:53 2018

@author: user
"""
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from numpy import math
import re

with open("C:\\Users\\user\\Desktop\\_chat.txt",encoding="utf-8") as file:
    
    data = []
    num = [str(x) for x in range(1,13)]
    
    for line in file:
        lines_c += 1
        search = re.search("(\d{1,2}).(\d{1,2}).(\d{4}),"+\
                           " (\d{1,2}):(\d{2}):(\d{2})",line)

        print(search if search==None else search.groups())
        temp = line   
        line = line[:-1].split(':')
        if len(line)>=4:
            sender = line[2][4:]
            message = ":".join(line[3:])
            sums += len(line)
            row = [x for x in search.groups()]+[sender,message,\
                   len(message)]
            if "<‏התמונה הושמטה>" in message:
                row+=[1,0,0]
            else:
                if " <‏קטע קול הושמט>" in message:
                    row+=[0,1,0]
                else:
                    if " <‏הסרט הושמט>" in message:
                        row+=[0,0,1] 
                    else:
                        row+=[0,0,0]
            data.append(row)
        else:
            if len(line)==1:
                count+=1
                sums +=len(line)
                print(line[0])

df = pd.DataFrame(data,columns=["day","month",\
                                "year","hour","minute","second",\
                                "sender","message","chars",\
                                "pic","voice","video"])

     
