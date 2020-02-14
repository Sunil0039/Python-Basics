# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:29:48 2020

@author: Sunil Kumar Singh
"""

###################### printing pattern using FOR Loops #################################

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
        

for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()   



for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()



for i in range(4):
    for j in range(4-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()



for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()



for row in range (7):
    for col in range (5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


for row in range (7):
    for col in range (5):
        if ((col>0 and col<4) and (row==0 or row==3 or row==6)) or (col==0 and (row==1 or row==2 or row==5)) or (col==4 and (row==1 or row==4 or row==5)):
            print("*",end="")
        else:
            print(" ",end="")
    print()


for row in range (4):
    for col in range (8):
        if row==0 or (row==1 and (col<3 or col>4)) or (row==2 and (col<2 or col>5)) or (row==3 and (col<1 or col>6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
