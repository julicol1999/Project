import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')  # Leer los datos

# Crear botones para cada gráfico
hist_button = st.checkbox('Construir histograma')
scatter_button = st.checkbox('Construir gráfico de dispersión')

if hist_button:  # Al hacer clic en el botón de histograma
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 

if scatter_button:  # Al hacer clic en el botón de dispersión
    # Escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)




