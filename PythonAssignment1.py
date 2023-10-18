#!/usr/bin/env python
# coding: utf-8

# In[2]:


l_limit=2000
u_limit=3200
for i in range(l_limit,u_limit+1,1):
    if(i%7==0 and i%5!=0):
        print(i,end=",")
print("\b")


# In[5]:


fn=input("Enter first name: ")
ln=input("Enter last name: ")
name= fn+" "+ln
rev_name=''
l=len(name)-1
for i in range(l,-1,-1):
    rev_name=rev_name+name[i]
print(rev_name)


# In[7]:


dm=12
rad=dm/2
vol=(4/3) * 3.14 * (rad*rad*rad)
print(vol)


# In[ ]:




