#!/usr/bin/env python
# coding: utf-8

# # Do all(10) math functions on your phone
# # Print all number between 1 and 100, print, odd, even, and prime.
# # Fuzz Buzz exampleWrite a program that prints the numbers from 1 to 100.
# # But for multiples of three print “Fizz” instead of the number
# # and for the multiples of five print “Buzz”.
# # For numbers which are multiples of both three and five print “FizzBuzz”.

# In[14]:


# Do all 10 Math functions on your phone
a = 3
b = 5
import math as mt
import numpy as np


# In[3]:


print ("The sum of",a,"and",b,"is", a+b)


# In[4]:


print ("The subtraction of",a,"and",b,"is", a-b)


# In[5]:


print ("The product of",a,"and",b,"is", a*b)


# In[6]:


print ("The division of",a,"and",b,"is", a/b)


# In[7]:


print ("The square of",a,"is", a**2)


# In[12]:


print ("The square root of",a,"is", mt.sqrt(a))


# In[15]:


print ("The log of",a,"is", mt.log(a))


# In[16]:


print ("The sine of",a,"is", mt.sin(a))


# In[17]:


print ("The cosine of",a,"is", mt.cos(a))


# In[18]:


print ("The tangent of",a,"is", mt.tan(a))


# In[19]:


# Print all numbers between 1-100, print odd, even, and prime


# In[22]:


for i in range (1,100):
    print (i)


# In[26]:


for i in range (1,100):
    if i%2>0:
        print (i)


# In[27]:


for i in range (1,100):
    if i%2==0:
        print (i)


# In[57]:


# primes, this was difficult and I had to use an online resource for advice
for i in range (1,100):
    prime = True
    for j in range (2,i):
        if (i%j==0):
            prime = False
    if prime == True:
        print (i)


# In[58]:


# Fuzz Buzz example. Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.


# In[77]:


for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    else:
        if i%3==0:
            print(i,"Fizz")
        else:
            if i%5==0:
                print(i,"Buzz")


# In[ ]:




