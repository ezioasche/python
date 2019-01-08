# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:31:09 2018

@author: Administrator
"""

def get_size(n):
    return len(str(n));
def get_digit(n):
    if n<10:
        return n
    elif(n<20)and(n>9):
        return (n-9)
def sum_of_double_even(n):
    sum=0
    i=0
    j=0
    list1=[]
    list1=list(str(n))
    list2=list1[::-1]
    if((get_size(n)%2)!=0):
        for i in range(0,get_size(n),2):
            j=get_digit((int(list2[i]))*2)
            sum+=j
    else:
        for i in range(1,get_size(n),2):
            j=get_digit((int(list2[i]))*2)
            print(j)
            sum+=j
    return sum
def sum_of_odd(n):
    i=0;
    sum=0;
    list1=[]
    list1=str(n)
    list2=list1[::-1]
    if((get_size(n)%2)!=0):
        for i in range(1,get_size(n),2):
            sum+=int(list2[i])
    else:
        for i in range(0,get_size(n),2): 
            sum+=int(list2[i])
    return sum
def is_vaild(n):
    if((sum_of_double_even(n)+sum_of_odd(n))/10==0):
        return True
    else:
        return False
print(sum_of_double_even(4388576018402626))
print(sum_of_odd(4388576018402626))
print(is_vaild(4388576018402626))
