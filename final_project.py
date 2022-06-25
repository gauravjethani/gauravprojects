#!/usr/bin/env python
# coding: utf-8

# 

# 
# 
# 
# ![](img/add_cell.png)
# 
# 
# 
# To make a new cell you can click on the **+** in the toolbar above.
# 
# To change the cell to a text cell, you can click on the ***Code*** dropdown menu above and change it to ***Markdown***.
# 
# Delete this cell (by right clicking and selecting ***Delete Cells***) before handing in your project. 

# Data Analysis for the Disney Movies

# Introduction : 

# In this analysis there will be analysis of various question associated with the collection of Disney movies.I am interested in finding out regarding the Disney movies dataset.

# Methods and Results

# I am  interested in computing the Disney Movies collection on the basis of the revenue as I will be conducting my analysis. This implies that I will only be using only **disney movies total gross** tables as that is only tables which has a relevant data for analysis.
# 
# However, before moving further, let us import the libraries and tables.

# 

# In[38]:


import altair as alt
import pandas as pd


# In[39]:


disney_movies = pd.read_csv('disney_movies_total_gross.csv')
disney_movies


# In[40]:


print(disney_movies.head(579))
for columns in disney_movies.total_gross:
    disney_movies['total_gross'] = disney_movies['total_gross'].str.replace(r'\W',"",regex=True)


# In[41]:


print(disney_movies.head(579))
for columns in disney_movies.inflation_adjusted_gross:
    disney_movies['inflation_adjusted_gross'] = disney_movies['inflation_adjusted_gross'].str.replace(r'\W',"",regex=True)


# As the dataset above is not cleaned and had dollar($) and comma(,) symbol inserted in the total_gross and inflation_adjusted_gross and had to remove those values which will help to sort data in ascending and the descending order to evaluate which movie has highest totalgross and lowest totalgross respectively based on the condition.

# In[42]:


disney_movies = disney_movies.rename(columns={'inflation_adjusted_gross':'gross_inflation'})
disney_movies


# Need to rename the inflation_adjusted_gross to gross_inflation for the analysis  

# In[43]:


disney_movies.dtypes


# In[44]:


disney_movies['release_date'] = pd.to_datetime(disney_movies.release_date)
disney_movies


# In[45]:


disney_movies['total_gross'] = disney_movies['total_gross'].astype(float)
disney_movies['gross_inflation'] = disney_movies['gross_inflation'].astype(float)


# In[46]:


disney_movies.dtypes


# The release_date,total_gross and inflation_adjusted_gross is not in a proper dtypes so conveted in a proper dtypes which will help to sort data based on the given condition

# In[47]:


disney_df = disney_movies.sort_values('total_gross',ascending = False)
disney_df


# Now that we have cleaned and have sorted the data based on the highest total_gross revenue earned by each Disney film and as it was obvious that Star Wars was the highest earning movie  

# In[48]:


disney = disney_df['total_gross'].astype('int').sum()
disney


# As the data was already cleaned above we need to find out what was the total gross revenue was earned by disney movies from  1937 until 2016 during this period.

# In[49]:


disney0= disney_df['total_gross'].astype('int').mean()
disney0


# We need to find out the mean for disney movies to know which movies has performed better and vice-versa  

# In[50]:


disney1 = disney_df[(disney_df['total_gross']>=disney0)]
disney1


# As we found out that 168  movies had performed better than the average and remainning all the movies were below average. 

# In[51]:


disney2 = disney_df['genre']
disney3 = disney2.value_counts()
disney3


# In[52]:


disney4 = disney1['genre']
disney5 = disney4.value_counts() 
disney5


# As the above 2 tables reflect data about various genre types and how many movies are there in each type in a dataset. The 1st table reflects all the movies category which has performed below and also includes those movies which has performed better than the average and in the second table it includes only those genre movies which has performed better than the average.

# In[53]:


disney6 = pd.DataFrame(disney_df.groupby('genre')['total_gross'].mean().sort_values(ascending=True)).astype('int64')
disney6 = disney6.reset_index()
disney6


# In[54]:


disney7 = pd.DataFrame(disney1.groupby('genre')['total_gross'].mean().sort_values(ascending=True)).astype('int64')
disney7 = disney7.reset_index()
disney7


# As the above 2 tables reflect data about various genre types and which genre type movies in a dataset has earned how much total gross revenue and what is the mean of those movies. 
# The 1st table reflects all the movies category which has performed below and also includes those movies which has performed better than the average and in the second table it includes only those genre movies which has performed better than the average and 3 genre movies type were not better than the average as well.

# In[55]:


disney8 = (
    alt.Chart(disney6,width = 500, height = 300)
    .mark_bar().encode(
        x = alt.X("genre:O",title = "Movies Type",sort="-y"),
        y=alt.Y("total_gross:Q", title="Gross Revenue"),
    )
    .properties(title = "Revenue by Movies Type")
)
disney8


# In[56]:


disney9 = (
    alt.Chart(disney7,width = 500, height = 300)
    .mark_bar().encode(
        x = alt.X("genre:O",title = "Movies Type",sort="-y"),
        y=alt.Y("total_gross:Q", title="Gross Revenue"),
    )
    .properties(title = "Revenue by Movies Type")
)
disney9


# In[57]:


disney10 = disney_df["release_date"].dt.year 
disney10


# In[58]:


disney11 = disney10.value_counts()
disney11


# As the above 2 tables I had converted release_date into year and than later on found how many movies were released in every year to find out the trend whether there is an increase in movies release or not.
# 
# 

# In[59]:


disney12 = pd.DataFrame({"year": disney11.index,"count":disney11.values})
disney12


# As wanted to plot in a graph wanted to have data in a tabular format to see how many Disney movies were released in every year.

# In[60]:


disney13 = (
    alt.Chart(disney12,width = 500, height = 300)
    .mark_bar().encode(
        x = alt.X("year:O",title = " Year of Disney Movies"),
        y=alt.Y("count:Q", title=" Total No. of Movies Release In a Year"),
    )
    .properties(title = "Movies Released year-wise")
)
disney13


# In the above chart it clearly states that disney movies has increased especially from 1985 year onwards amd in 1995 it was the highest movies release but after 1995 there was a drop in disney movies release but it was releasing a sufficent movies on yearly basis. Also some of the highest grossing movies were released especially after 2010 which has been noticed where we had done our analysis above in disney_df
# 
# 

# In[61]:


disney14 = disney_df
disney14


# In[62]:


disney14["year"] = disney14["release_date"].dt.year
disney14


# As wanted to evaluate in which year disney movies has earned highest gross revenue based on year as the data was in the yyyy-mm-dd format so wanted to convert in a year to find out how much total revenue was generated in each year
# 
# 

# In[63]:


disney15 = pd.DataFrame(disney14.groupby('year')['total_gross'].sum()).astype('int64')
disney15 = disney15.reset_index()
disney15


# In[64]:


disney16 = (
    alt.Chart(disney15,width = 500, height = 300)
    .mark_bar().encode(
        x = alt.X("year:O",title = "Revenue Year Wise",sort="-y"),
        y=alt.Y("total_gross:Q",title="Sum of Gross Revenue of all movies released in a year"),
    )
    .properties(title = "Sum of Revenue based on year wise")
)
disney16


# As in the above graph shows that even though in the previous chart we saw that number of movies release has decreased but substancial movies were released and the revenue was highest in the year 2016 even though no. of movies was not highest. Also the trend of highest revenue is in the decending order from 2016 for majorly for most of the years and 2016 being the highest revenue earned during that year.
# 
# 

# ## References

# Not all the work in this notebook is original. Some parts were borrowed from online resources
# 
# 

# * [Codes for Python](https://stackoverflow.com/)
#     * The codes used in this project was taken from **Stackoverflow**
# * [Codes for Python](https://pandas.pydata.org)
#     * The codes used in this project was taken from **Pandas Pydata**
# * [Codes for Python](https://www.kaggle.com/discussion)
#     * The codes used in this project was taken from **Kaggle**

# In[ ]:





# In[ ]:




