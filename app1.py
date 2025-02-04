import streamlit as st
import pandas as pd
import plotly.express as px
# Crear un DataFrame de ejemplo
data = {
    "Categoría": ["A", "B", "C", "D", "E"],
    "Valores": [23, 45, 56, 78, 33]
}
df = pd.DataFrame(data)
st.set_page_config(page_title='MI APP',page_icon='smile',layout='wide' # Layout expande a toda la pagina
                )
def main():
    st.sidebar.header("Navegación")# barra lateral
    st.title("curso de streamlit")
    # Crear el gráfico de barras
    fig = px.bar(df, x="Categoría", y="Valores", title="Gráfico de Barras con Plotly Express",color="Categoría")
    st.plotly_chart(fig)


if __name__ == '__main__':
        main()