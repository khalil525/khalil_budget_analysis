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

st.markdown('### Lets talk MONEY $$$') 

col1, col2, col3 = st.columns(3)

with col1:
    Income = st.number_input('What is your bi-weekly take home pay?')
with col2:
    Expenses = st.number_input('What is the total of your bi-weekly expenses?')
with col3:
    Left_Overs = st.number_input('Is there a certain amount of money you want have left over by your next pay check?')
    
Remaining = Income - Expenses - Left_Overs

st.markdown('---') 

st.markdown(f'You have ${Remaining} after your expenses!') 

st.markdown('---') 


# ---- ROW B ---- 

col1, col2, col3, col4 = st.columns(4)

with col1:
    Emergency_Actual = st.number_input('How much have you put into your Emergency Savings?')
with col2:
    Retirement_Actual = st.number_input('How much money have you put into Your Retirement Savings?')
with col3:
    Food_and_Drinks_Actual = st.number_input('How much money have you spent on food and drinks?')
with col4:
    Transportation_Actual = st.number_input('How much money have you spent on Transportation?')
    
# ---- ROW C ---- 
st.markdown('---') 

col1, col2, col3, col4 = st.columns(4)

with col1:
    Entertainment_Actual = st.number_input('How much money have you spent on entertainment?')
with col2:
    Miscellaneous_Actual = st.number_input('How much money have you pulled from your Miscellaneous fund?')
with col3:
    Debt_Actual = st.number_input('How much money have you put towards your debt?')
with col4:
    Business_Actual = st.number_input('How much money have you invested in your business?')

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

st.markdown('---') 



# In[ ]:


# ---- DATA ---- 
# data = [["Emergency Savings", (Emergency * Remaining) - Emergency_Actual],
 #      ["Retirement Savings", (Emergency * Remaining) - Emergency_Actual],
   #    ["Food/Drinks", (Emergency * Remaining) - Emergency_Actual]
    #   ["Transportation Savings", (Emergency * Remaining) - Emergency_Actual]
     #  ["Entertainment", (Emergency * Remaining) - Emergency_Actual]
  #     ["MISC", (Emergency * Remaining) - Emergency_Actual]
  #     ["Debt Payments", (Emergency * Remaining) - Emergency_Actual]
   #    ["Bussiness/Investing", (Emergency * Remaining) - Emergency_Actual]]



emergency_actual = Emergency * Remaining - Emergency_Actual



data = { "Budget Category" : ["Emergency Savings", "Retirement Savings","Food/Drinks",
                             "Transportation", "Entertainment", "MISC", "Debt Payments",
                             "Business/Investments"],
        "Difference of Budget and Expenditures" : [ emergency_actual,
                                                   Retirement * Remaining - Retirement_Actual,
                                                   Food_and_Drinks * Remaining - Food_and_Drinks_Actual,
                                                   Transportation * Remaining - Transportation_Actual,
                                                   Entertainment * Remaining - Entertainment_Actual,
                                                   MISC * Remaining - Miscellaneous_Actual,
                                                   Debt * Remaining - Debt_Actual,
                                                   Business * Remaining - Business_Actual]}


st.markdown('The table and chart below shows you how much money you have left to spend for the next two weeks in each Budget category based on the information provide.') 

df = pd.DataFrame(data )
st.dataframe(df) 


# In[ ]:


# ---- FUNNEL CHART  ---- 
# fig_funnl_chart = px.funnel(df, x='Difference of Budget and Expenditures', 
                           # y='Budget Category',
                           # title = "<b>Budget Tracker</b>",
                           # template = "plotly_white")

# st.plotly_chart(fig_funnl_chart)c
st.markdown('---') 
st.markdown('Budget Tracker') 

st.bar_chart(data = df, x = "Budget Category", y = 'Difference of Budget and Expenditures')

