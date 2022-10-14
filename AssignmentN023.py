#!/usr/bin/env python
# coding: utf-8

# # Assignment 23 Solutions

# 1.Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

# In[1]:


def is_symmetrical(in_num):
    if str(in_num) == str(in_num)[::-1]:
        print(f'{in_num}-->{True}')
    else:
        print(f'{in_num}-->{False}')
        
is_symmetrical(7227)
is_symmetrical(12567)
is_symmetrical(44444444)
is_symmetrical(9939)
is_symmetrical(1112111)


# 2.Given a string of numbers separated by a comma and space, return the product of the numbers.

# In[2]:


def multiply_num(in_string):
    out_string = in_string.replace(' ','').split(',')
    out_num = 1
    for i in out_string:
        out_num*= int(i)
    print(f'{in_string}-->{out_num}')
    
multiply_num("2,3")
multiply_num("1,2,3,4")
multiply_num("54,75,453,0")
multiply_num("10,-2")


# 3.Create a function that squares every digit of a number.

# In[3]:


def square_digits(in_num):
    in_list = [str(int(i)**2) for i in str(in_num)]
    out_list = ''.join(in_list)
    print(f'{in_num}-->{int(out_list)}')
    
square_digits(9119)
square_digits(2483)
square_digits(3212)


# 4.Create a function that sorts a list and removes all duplicate items from it.

# In[4]:


def satify(in_list):
    out_list = sorted(set(in_list))
    print(f'{in_list}-->{out_list}')

satify([1,3,3,5,5])
satify([4,4,4,4])
satify([5,7,8,9,10,15])
satify([3,3,3,2,1])


# 5.Create a function that returns the mean of all digits.

# In[5]:


def mean(in_num):
    in_list = [int(i)for i in str(in_num)]
    out_num = sum(in_list)/len(str(in_num))
    print(f'mean of {in_num}-->{out_num:.0f}')
mean(42)
mean(12345)
mean(666)


# In[ ]:




