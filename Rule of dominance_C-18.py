# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:55:29 2021

@author: Admin
"""

#ENTER PAYOFF MATRIX
import numpy as np 

matrix=[]
row = int(input('Enter the number of rows'))
col = int(input('Enter the number of columns'))
for i in range (row):#0,1,2
    a = []
    for j in range (col):#0,1,2
        val=int(input("Enter the number: "))
        a.append(val)
    matrix.append(a)
arr = np.array(matrix)
for i in range (row):#for display
    for j in range (col):
        print(arr[i][j],end=" ")
    print()
    


count1=0
count2=0
size=row-1
width=col-1
i=0
j=0
r=1
arr_1=arr.copy()
for i in range (row):
    count1=0
    count2=0
    for r in range (1,row):
        for j in range (col):
            if (i<row) and (i+r<row) and (arr[i][j] != -1) and (arr[i+r][j] != -1):
                if arr[i][j] >= arr[i+r][j]:
                    count1+=1
                else:
                    count2+=1
            else:
                break
            if count1 == col:
                print('i',i)
                arr[i+1,:]=-1
            if count2 == col:
                print('i',i)
                arr[i,:]=-1
        
print(arr)
for j in range (row):
    count1=0
    count2=0
    for r in range (1,col):
        for i in range (row):
            '''
            if (arr[i][j] != -1) and (arr[i][j+r] != -1):
                    i+=1
                    '''
            if (j<width) and (j+r<col) :
                if arr[i][j] <= arr[i][j+r]:
                    count1+=1
                else:
                    count2+=1
            else:
                break
            if count1 == row:
                arr[:,j+1]=-1
            if count2 == row:
                arr[:,j]=-1
print(arr)
for i in range (row):#for display
    for j in range (col):
        print('The Value of game is',arr[i][j]!=-1,arr[i][j])
                
        
    
        
           
            
    









    
    





    

    

