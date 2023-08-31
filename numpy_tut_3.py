#!/usr/bin/env python
# coding: utf-8

# In[3]:


#there is slicing in list we do usually
li =[3, 5, 6, 7]
li[0:2]   #it doesnt include last one i mean(index=2)
li[-1]    #acces from end through index=-1


# In[6]:


#here we do indexing in aray 
import numpy as np
a=np.array([1, 2, 3, 4, 5])   #one dimensional aray
a[0:3]                        #it doesnt include last one i mean(index=3)
a[-1]                         #acces from end through index=-1


# In[9]:


#here we have a multidimensional array
import numpy as np 
A=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A


# In[10]:


A[1, 2]   #means row with index 1 and column with index 2 (element will bw fetched )


# In[11]:


#if we do slicing in row and column and tell which elements should be printed
A[0:2, 2]           #means go to row 0 and row 1 and select elemnt at index 2 from both rows 


# In[14]:


# -1 will bring last row 
A[-1]


# In[15]:


A[-1, 0:2]    #vist column 0 and 1 , and print last row of col 0 to 2 or last elements of these cols


# In[16]:


A[:, 1:]          # all rows but except 0th column 


# In[17]:


#lets see how we can iterate throgh array
for row in A:
    print(row)


# In[18]:


#convert array into single dimensional array and iterate through each element not entire row
for cell in A.flat:
    print(cell)


# In[23]:


#we can stack two arrays 
a=np.arange(6).reshape(3, 2)
b=np.arange(6, 12).reshape(3, 2)
a, b
np.hstack((a,b))    #horizontal stack 


# In[24]:


#verticcal stack
np.vstack((a,b))


# In[28]:


# randomly creating an array with 2 rows and 15 columns
w=np.arange(30).reshape(2, 15)
w
#arange(30), upto range 30 


# In[33]:


#split this array(w) into three arrays 
result =np.hsplit(w, 3)
result[0]


# In[31]:


result[1]


# In[32]:


result[2]


# In[40]:


#lets do a vertical split
result2 =np.vsplit(w, 2)
result2[0]


# In[ ]:




