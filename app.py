import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise exploratória de veículos')

car_data = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando um gráfico de dispersão')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)