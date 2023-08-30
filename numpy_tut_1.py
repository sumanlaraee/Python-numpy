#!/usr/bin/env python
# coding: utf-8

# In[9]:


#numpy is extremely popular module in python , heavily used in scientific computing 
#advantages of numpy::(fast, ndimensional array, less memory , convinient )
import numpy as np 
import sys
import time


# In[10]:


l = range(1000)   #list of 1000 elements 
print(sys.getsizeof(5)*len(l))   #iam gonna print size of list 
#sys is module in python provide size object 
#(sys.getsizeof(5) here 5 is integer type an element and this line returns the size of element in byte 
#len(l)   return the number of elements in list (length of list )
#everything is object so pointer's list is there


# In[12]:


array =np.arange(1000)  #arange is same as range 
print(array.size * array.itemsize ) #itemsize is size of single element, array.size is size of entire array


# In[19]:


#let's see how numpy is faster than list 
size =1000

la = range(1000)
lb=range(10000000)

a1=np.arange(size)
a2=np.arange(size)

#list
start=time.time()
result=[(x+y)for x, y in zip(la, lb)]
print("time list took",(time.time()-start)*1000)

# numpyarray 
start=time.time()
result=a1+a2

print("time array took:", (time.time()-start)*1000)

# here you can see numpy is crazy fast


# In[22]:


#how numpy is convinient 
a1=np.array([1, 2, 3])
a2=np.array([4,5, 6])
print(a1+a2)
print(a2-a1)


# In[ ]:




