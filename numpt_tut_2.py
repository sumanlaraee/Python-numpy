#!/usr/bin/env python
# coding: utf-8

# In[4]:


#here we gonna learn more about numpy 
import numpy as np 
#this is one d array in python
a1=np.array([11, 2, 3])
a1[0]   #access element through index 


# In[5]:


#this is two d array
a2=np.array([[1,2 ,3], [3, 4, 5], [6, 7, 8]])
a2. ndim               #use ndim object to print dimensions 


# In[6]:


# print  the number of bytes taken these are integers( take 4 bytes )
a2. itemsize


# In[7]:


#print datatype 
a2.dtype


# In[15]:


#we can change type (from int to float , float to complex )
a2=np.array([[1,2 ,3], [3, 4, 5], [6, 7, 8]]   ,dtype=np.float64)
a2. itemsize    #item size went from 4 to 8 b/c it became float instead of int 
a2     #lets check array 


# In[12]:


#number of elements in a array
a2.size 


# In[13]:


#number of rows and number of columns 
a2.shape


# In[17]:


#we can change type (from  float to complex
a2=np.array([[1,2 ,3], [3, 4, 5], [6, 7, 8]]   ,dtype=complex)
a2


# In[18]:


# we can change element's value 
np.zeros((3, 3))


# In[19]:


# we can change element's value 
np.ones((3, 3))


# In[22]:


#creating a random list to range 5 (Note: 5 itself is excluded )
ls = range(5)
ls[0]
ls[4]
#ls[5] it is an error of range object index out of range


# In[24]:


#creating a random randm array of 5 elements 5 iant included 
np.arange(1, 5)


# In[26]:


# gap of numbers btw number generation in a particular range 
np.arange(1, 5, 2)
# numbers are being generated btw 1 and 5 with jump of 2 (1+2 =3)


# In[44]:


a3=np.array([[1,2, 4],
    [2,4,6]])
#we can reshape an array
a3.shape   #it has (2, 3) shape 


# In[45]:


#reshape to (3, 2)
a3.reshape(3, 2)


# In[46]:


# flatten or make an array one dimentional from many dimensions but not permanatly just a copy 
a3.ravel()


# In[52]:


#minimun and maximum array , sum all elements 
a3.min()
a3.max()
a3.sum()


# In[54]:


#axis (dimension )  axis =0 for columns, axis =1, for rows , all eleemnts of each column will be seprately added 
a3.sum(axis=0)
a3.sum(axis=1)


# In[55]:


#find sqre root of array sqrt comes from np module 
np.sqrt(a3)


# In[56]:


#we can find an standard deviation  comes from np module 
np.std(a3)


# In[57]:


#something you cant do with python native list is add two 2d arrays 
x=np.array([[1,2], [2, 4]])
y=np.array([[1, 4],[5, 7]])
x+y


# In[58]:


#other operation with 2d arrays can be done same way ie.(-, /, *)
x.dot(y)          #this is a matrix product


# In[ ]:




