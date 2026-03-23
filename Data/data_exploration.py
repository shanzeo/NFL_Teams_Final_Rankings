#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv('team_stats_2003_2023.csv')
df.head()


# In[5]:


df.columns


# In[6]:


df.shape


# In[7]:


missing_rows = df[df.isna().any(axis=1)]

print("\nRows with missing values:")
print(missing_rows)

