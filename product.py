# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:26:49 2020

@author: S.Narain Ramaswamy
"""

from multipledispatch import dispatch 

  
#passing one parameter 
@dispatch(int,int) 
def product(first,second): 
    result = first*second 
    print(result); 
  
#passing two parameters 
@dispatch(int,int,int) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
#you can also pass data type of any value as per requirement 
@dispatch(float,float,float) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
  
#calling product method with 2 arguments 
product(3,4)
product(2,3,10) #this will give output of 12 
product(2.2,3.4,2.3) # this will give output of 17.985999999999997 
