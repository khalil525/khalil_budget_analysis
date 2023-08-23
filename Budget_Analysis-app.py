#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[4]:


import pandas as pd
import streamlit as st 
#import plotly.express as px 


# In[ ]:


st.set_page_config(page_title = "Budget Analysis",
                   page_icon = ":bar:",
                  layout = "wide",
                   initial_sidebar_state = 'expanded'
                  ) 


# In[ ]:


# ---- ROW A ---- 

st.markdown('### Lets talk MONEY') 

col1, col2, col3 = st.columns(3)

with col1:
    Income = st.slider('What is your bi-weekly take home pay?',
                           0, 10000, 1000)
with col2:
    Expenses = st.slider('What is the total of your bi-weekly expenses?',
                      0, 10000, 1000)
with col3:
    Left_Overs = st.slider('Is there a certain amount of money you want have left over by your next pay check?',
                             0, 10000, 1000)
    
Remaining = Income - Expenses - Left_Overs

st.markdonwn('---') 

st.markdown(f'You have ${Remaining} after your expenses!') 

st.markdonwn('---') 


# ---- ROW B ---- 

col1, col2, col3, col4 = st.columns(4)

with col1:
    Emergency_Actual = st.slider('How much have you put into your Emergency Savings?',
                           0, 10000, 1000)
with col2:
    Retirement_Actual = st.slider('How much money have you put into Your Retirement Savings?',
                      0, 10000, 1000)
with col3:
    Food_and_Drinks_Actual = st.slider('How much money have you spent on food and drinks?',
                             0, 10000, 1000)
with col4:
    Transportation_Actual = st.slider('How much money have you spent on Transportation?',
                             0, 10000, 1000)
    
# ---- ROW C ---- 

col1, col2, col3, col4 = st.columns(4)

with col1:
    Entertainment_Actual = st.slider('How much money have you spent on entertainment?',
                           0, 10000, 1000)
with col2:
    Miscellaneous_Actual = st.slider('How much money have you pulled from your Miscellaneous fund?',
                      0, 10000, 1000)
with col3:
    Debt = st.slider('How much money have you put towards your debt?',
                             0, 10000, 1000)
with col4:
    Business_Actual = st.slider('How much money have you invested in your business?',
                             0, 10000, 1000)

# ---- SIDEBAR ---- 

st.sidebar.header("Make changes based on your budget and spending habits") 

Emergency = st.sidebar.slider('What percentage of your income would you like to go towards Emergency Savings?',
                          0.01, 1.00, .10)

Retirement = st.sidebar.slider('What percentage of your income would you like to go towards Retirement Savings?',
                          0.01, 1.00, .10)

Food_and_Drinks = st.sidebar.slider('What percentage of your income would you like to go towards Food/Drinks?',
                          0.01, 1.00, .10)

Transportation = st.sidebar.slider('What percentage of your income would you like to go towards Transportation?',
                          0.01, 1.00, .10)

Entertainment = st.sidebar.slider('What percentage of your income would you like to go towards Entertainment?',
                          0.01, 1.00, .10)

MISC = st.sidebar.slider('What percentage of your income would you like to go towards a Miscellaneous fund?',
                          0.01, 1.00, .10)

Debt = st.sidebar.slider('What percentage of your income would you like to go towards debt payments?',
                          0.01, 1.00, .10)

Business = st.sidebar.slider('What percentage of your income would you like to go towards funding your Business?',
                          0.01, 1.00, .10)




# In[ ]:


# ---- DATA ---- 
data = [["Emergency Savings", (Emergency * Remaining) - Emergency_Actual],
       ["Retirement Savings", (Emergency * Remaining) - Emergency_Actual],
       ["Food/Drinks", (Emergency * Remaining) - Emergency_Actual]
       ["Transportation Savings", (Emergency * Remaining) - Emergency_Actual]
       ["Entertainment", (Emergency * Remaining) - Emergency_Actual]
       ["MISC", (Emergency * Remaining) - Emergency_Actual]
       ["Debt Payments", (Emergency * Remaining) - Emergency_Actual]
       ["Bussiness/Investing", (Emergency * Remaining) - Emergency_Actual]]

df = pd.DataFrame(data, columns = ['Budget Category', 'Difference of Budget and Expenditures'] )
st.dataframe(df) 


# In[ ]:


# ---- FUNNEL CHART  ---- 
# fig_funnl_chart = px.funnel(df, x='Difference of Budget and Expenditures', 
                           # y='Budget Category',
                           # title = "<b>Budget Tracker</b>",
                           # template = "plotly_white")

# st.plotly_chart(fig_funnl_chart)c

st.bar_chart(data = df, y = "Budget Category", x = 'Difference of Budget and Expenditures')

