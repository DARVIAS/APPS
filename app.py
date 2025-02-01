import streamlit as st
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
})

# Crear un gráfico interactivo con Plotly
fig = px.line(df, x="x", y="y", title="Gráfico interactivo")

# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(fig)