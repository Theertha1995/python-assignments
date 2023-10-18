#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=5
for i in range(1,n,1):
    for j in range(0,i,1):
        print("*", end=" ")
    print("\b")
for k in range(n-1,-1,-1): 
    for l in range(k,-1,-1):
        print("*", end=" ")
    print("\b")


# In[5]:


word= input("Enter a string : ")
print(word[::-1])


# In[ ]:




