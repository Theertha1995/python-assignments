#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1.1 Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()
def myreduce(myfuction,mylist):
    result=mylist[0]
    for i in mylist[1:]:
        result=myfuction(i,result)
    return result

def addNums(a,b):
    return a+b

def maxValue(a,b):  
    if a > b:
        return a
    else:
        return b

mylist=[30,10,50,20,40]
sumofNums=myreduce(addNums,mylist)
print(sumofNums)
maxval=myreduce(maxValue,mylist)
print(maxval)


# In[20]:


#1.2 Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()
def myfilter(myfunction,mylist):
    result=[]
    for i in mylist:
        if(myfunction(i)):
            result.append(i)
    return result

def oddNums(x):
    if(x%2==1):
        return True

def multipleOf3(x):
    if(x%3==0):
        return True

mylist=[5,2,7,3,8,4,9,1,6]
oddresult=myfilter(oddNums,mylist)
print("Odd numbers: ",oddresult)

multipleOf3result=myfilter(multipleOf3,mylist)
print("Multiple of 3: ",multipleOf3result)


# In[24]:


# 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
inputlist=['x','y','z']
newlist=[i*j for i in inputlist for j in range(1,5)]
print(newlist)


# In[27]:


#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
inputlist=['x','y','z']
newlist=[i*j for i in range(1,5) for j in inputlist]
print(newlist)


# In[35]:


#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
inputlist=[2,3,4]
newlist=[[i+j] for i in range(0,3) for j in inputlist]
print(newlist)


# In[37]:


#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
inputlist=[2,3,4,5]
newlist=[[i+j for i in range(0,4)] for j in inputlist]
print(newlist)


# In[54]:


#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
inputlist=[1,2,3]
newlist=[(j,i) for i in inputlist for j in inputlist]
print(newlist)


# In[ ]:




