# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 08:57:27 2021

@author: rutaz
"""

import csv

arr = []

with open ("sample.csv",'r') as csvfile:
    for row in csv.reader(csvfile):
        arr.append(row)
    #print(arr[0][0])
    
ans = []

for i in range(len(arr[1])-1):
    ans.append("ϕ")
    
for i in range(1,len(arr)):
    for j in range(len(arr[1])-1):
        if ans[j] == "?" or arr[i][len(arr[1])-1] == "no":
            continue
        elif ans[j] == "ϕ":
            ans[j] = arr[i][j]        
        elif arr[i][j] != ans[j]:
            ans[j] = "?"
    print(ans)

print("\n\n Final answer: " , ans)
            