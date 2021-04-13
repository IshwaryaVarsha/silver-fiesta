#!/usr/bin/env python
# coding: utf-8

# # Using Pandas-To analyse Olympics Data:

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


olympic=pd.read_csv('olympics.csv',skiprows=4)
olympic


# In[4]:


print('Total Rows:', olympic.shape[0]); print('Total Columns:', olympic.shape[1]);


# In[5]:


print('Total Number of Rows & Columns:', olympic.shape)


# In[7]:


olympic.head(n=10)


# In[8]:


olympic.tail(n=10)


# In[9]:


olympic.info()


# In[10]:


olympic.describe()


# In[12]:


olympic.columns.values


# In[13]:


olympic.index.values


#  # ANALYSING THE  OLYMPICS DATA 
1.In Which events did Edwin Flank win a medal?
# In[14]:


olympic['Athlete'][:30]


# In[15]:


EF=olympic[(olympic['Athlete']==' FLACK, Edwin')]
EF

2.Which country has won the most men's gold in Athletes over the years? Sort the results alphabetically by the players name
# In[16]:


gold_medal = olympic[(olympic.Medal == 'Gold') & (olympic.Gender == 'Men') & (olympic.Sport == 'Athletics')]
gold_medal


# In[17]:


mens = gold_medal.sort_values(by = 'Athlete')


# In[18]:


mens['NOC'].value_counts()[:10]


# In[19]:


len(mens['NOC'].value_counts())

3. How many gold medals the Indian Men's have won and name the event also ?
# In[20]:


data_IGold = olympic[(olympic['NOC']=='IND') & (olympic['Medal']=='Gold') & (olympic['Gender']=='Men')]
data_IGold


# In[24]:


data_IGold['Event'].value_counts()

4. Check to see how many Indian women's have won the gold, silver or branze medals in the Olympic games?
# In[23]:


olympic[(olympic['NOC']=='IND') & (olympic['Medal']=='Gold') & (olympic['Gender']=='Women')]


# In[26]:


olympic[(olympic['NOC']=='IND') & (olympic['Medal']=='Silver') & (olympic['Gender']=='Women')]


# In[27]:


olympic[(olympic['NOC']=='IND') & (olympic['Medal']=='Bronze') & (olympic['Gender']=='Women')]

5. Which five countries have won the most medals in recent years (from 2000 to 2008)?
# In[28]:


rec_medals = olympic[(olympic['Edition'] >= 2000)]
rec_medals


# In[30]:


recent_medals = rec_medals.sort_values(by='Edition', ascending=False)
recent_medals


# In[31]:


recent_medals['NOC'].value_counts().head(n=5)

6. Display the male gold medal winners for the hockey event over the years. List the results starting with the most recent. Show the Olympic City, Edition, Athlete and the country they represent.
# In[33]:


olympic['Event'].value_counts().head(n=10)


# In[34]:


male_gold_hundred = olympic[(olympic.Gender == 'Men') & (olympic.Medal == 'Gold') & (olympic.Event == 'hockey')]
male_gold_hundred


# In[35]:


male_gold_hundred.sort_values(by = 'Edition', ascending=False )


# In[36]:


male_gold_hundred.sort_values(by = 'Edition', ascending=False )[['City','Edition','Athlete','NOC']]

7. How many women's have won the gold medal's till 2008 in Olympic game
# In[37]:


women_gold = olympic[(olympic.Medal == 'Gold') & (olympic.Gender == 'Women')]
women_gold


# In[38]:


women_gold.sort_values(by ='Athlete')


# In[39]:


women_gold['Athlete'].drop_duplicates()


# In[40]:


women_gold.sort_values(by ='Athlete', ascending=True )['Athlete'].value_counts()


# In[ ]:




