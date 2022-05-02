# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""

import pandas as pd
import streamlit as st
from datetime import date
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from pickle import dump
from pickle import load
from statsmodels.tsa.holtwinters import Holt

st.title('Gold Price Forecasting')

st.sidebar.header('GROUP 3')
st.sidebar.subheader('Chandrika K J')
st.sidebar.subheader('H Vishal')
st.sidebar.subheader('Nilakantha Panigrahi')
st.sidebar.subheader('H Shiva Nandini')
st.sidebar.subheader('Deepak Kumar Sharma')

st.sidebar.subheader('')
st.sidebar.subheader('')
st.sidebar.subheader('')

st.sidebar.header('Mentor')
st.sidebar.subheader('Karthik')


n_days = st.number_input("Enter number of days",0,150)
period = n_days

data = pd.read_csv(r"C:\Users\nilka\Project\DEPLOYMENT\Gold_data.csv",date_parser=['date'])
st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['date'], y=data['price'],name="data"))
	fig.layout.update(title_text='Time Series data', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
    
plot_raw_data()

## Load the model
loaded_model = load(open(r'C:\Users\nilka\Project\DEPLOYMENT\hw_model.sav', 'rb'))
X=period
column_names = ['Price']
pred=pd.DataFrame(loaded_model.forecast(X),columns=column_names)
st.subheader('Forecasted data')
pred
st.line_chart(pred)