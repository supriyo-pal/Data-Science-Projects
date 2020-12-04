#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np


# In[3]:


data=pd.read_csv("F:\Python Practice\Data Science\Covid 19 data Analysis\day_wise.csv")


# In[4]:


data


# In[5]:


data.head()


# # Relating the Variables with Scatter Plot

# In[6]:


data.columns


# In[22]:


sns.relplot(x='Confirmed',y='Deaths',data=data,hue="Deaths")


# # By analysing this dataset I have realised that the Deaths are increasing if it is a confirmed case

# In[8]:


sns.relplot(x='Confirmed',y='Deaths',data=data,kind='line')


# In[23]:


sns.relplot(x='Confirmed',y='Deaths',data=data,hue='Confirmed')


# # Confirmed cases are also increasing

# In[18]:


sns.relplot(x='Confirmed',y='Recovered',data=data,hue="Recovered")


# # Those who are having strong immunity system and also maintaing the rules of Government, Recovered even after the case is confirmed

# In[17]:


sns.relplot(x='Recovered',y='Deaths',data=data,hue="Recovered")


# In[20]:


sns.relplot(x='Confirmed',y='No. of countries',data=data,hue="Confirmed")


# # Here we have realised that number of cases are increasing in the cities

# In[21]:


sns.pairplot(data)


# 
