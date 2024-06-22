#!/usr/bin/env python
# coding: utf-8
Name - Jash 
LinkedIN - https://www.linkedin.com/in/jash-moze-166b11253/Profigy InfoTech Task-1
Create a bar chart or histogram to visualize the distribution of a categorial or continuous variable, such as the distribution of ages or genders in a populationImporting the necessary Libraries.
# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

Reading the data
# In[5]:


data = pd.read_csv("population.csv")


# In[6]:


data.head(266)


# In[7]:


data.describe


# In[16]:


#List of contries for the graph.
countries_to_plot = ['United States', 'Canada', 'Brazil', 'Japan', 'Germany', 'France']

#Filtering the data frame
filtered_data = data[data['Country Name'].isin(countries_to_plot)]

#Creating the bar chart
plt.bar (filtered_data['Country Name'], filtered_data['2022'])
plt.xlabel ('Country Name')
plt.ylabel ('Population in 2022')
plt.title('Population of selected countries in 2022')
plt.xticks(rotation=45, ha='right') #Rotating the x-axis labels for readability
plt.show()


# In[ ]:




