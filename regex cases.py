#!/usr/bin/env python
# coding: utf-8

# In[28]:


import re

random_text = '''
My name is Mr. Neo. My phone number is 123-456-7890. My email is ChosenOne@gmail.com
My name is Mr. Morphius. My phone number is 413-234-2568. My email is CoolGuy@yahoo.com. 
My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl1@apple.com.
'''

matches = re.findall('@([a-z]+)', random_text)
print(matches)


# In[19]:


matches = re.findall(r'@([\w\.]+)', random_text)
print(matches)


# In[27]:


matches = re.findall(r'[\w.+-]+@[\w.-]+', random_text)
print(matches)


# In[30]:


matches = re.findall(r'\d{3}-\d{3}-\d{4}', random_text)
print(matches)


# In[ ]:


my_list = ['ChosenOne@gmail.com', 'CoolGuy@yahoo.com.', 'ChosenOnesGirl1@apple.com.']


# In[33]:


import re

my_list = ['ChosenOne@gmail.com', 'CoolGuy@yahoo.com.', 'ChosenOnesGirl1@apple.com.']

for email in my_list:
    cleaned_email = email.rstrip('.')
    domain = re.findall(r'@([\w.]+)', cleaned_email)
    print(domain)


# In[37]:


import re

my_list = ['ChosenOne@gmail.com', 'CoolGuy@yahoo.com.', 'ChosenOnesGirl1@apple.com.']

domain_list = [
    re.findall(r'@([\w.]+)', email.rstrip('.'))[0]
    for email in my_list
    if re.findall(r'@([\w.]+)', email.rstrip('.'))
]

print(domain_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




