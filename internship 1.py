#!/usr/bin/env python
# coding: utf-8

# In[5]:


i = int(input("enter number"))
fac=1
while(i>0):
    fac=fac*i
    i=i-1
    print("Factorial=",fac)


# In[4]:


n=int(input("enter number"))
count=0
i=1
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime Number")
else:
    print("composite Number")
    


# In[6]:


a = input("enter string")
b=a[-1::-1]
if(a==b):
    print("palindrome string")
else:
    print("Not Palindrome String")


# In[9]:


from math import sqrt
a=float(input("Enter A: "))
b=float(input("Enter B: "))
c= sqrt(a**2 +b**2)
print ("the length ofthe third side:  ",c)


# In[13]:


a=float(input("Enter A: "))
b=float(input("Enter B: "))
c=(a**2 +b**2)
print ("the length ofthe third side:  ",c)


# In[3]:


from collections import Counter
test_str="pankajshaw"
res=Counter(test_str)
print(str(res))


# In[ ]:




