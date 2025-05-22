import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date','Category','amount','description'])


def add_expense(date,category,amount,description):
    new_data = pd.DataFrame([[date,category,amount,description]], columns=st.session_state.expenses.columns,)
    st.session_state.expenses = pd.concat([new_data,st.session_state.expenses],ignore_index=True)
  
def save_exp():
    st.session_state.expenses.to_csv('expenses.csv',index=False)
    st.success('File saves as expenses.csv')
    

def load_exp():
    uploaded_file = st.file_uploader('Chose a file',type=['csv'])
    if uploaded_file is not None:
        st.session_state.expenses = pd.read_csv(uploaded_file)
    else:
        st.write('select a valid file')


with st.sidebar:

    st.header('Daily Expense')
    date = st.date_input('Select Date')
    category = st.selectbox('Select Category',['Food','Travel','Education','Entertainment','other'])
    amount   = st.number_input('Enter Amount')
    description = st.text_input('description')
    if st.button('Add'):
        st.success('Expense Added')
        add_expense(date,category,amount,description)
    st.header('File Operations')
    if st.button('Save Expneses'):
        save_exp()
    if st.button('Load Expenses'):
        load_exp()


st.title('Daily Expense Tracker')
st.write(st.session_state.expenses) 

  
def visualise_exp():
    if not st.session_state.expenses.empty:
        fig,ax = plt.subplots()
        sns.barplot(data=st.session_state.expenses,x='Date',y='amount',hue='Category',ax=ax)
        st.pyplot(fig)

    else:
        st.warning ('no information available')
    

st.title('Visualization')
if st.button('Visualize'):
    visualise_exp()


