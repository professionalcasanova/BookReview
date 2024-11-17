import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# load dos arquivos.
df_reviews = pd.read_csv("C:/Users/masuc/Desktop/ArquivosPython/customer reviews.csv")
df_top100_books = pd.read_csv("C:/Users/masuc/Desktop/ArquivosPython/Top-100 Trending Books.csv")

# Filtros gráficos.
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()
price = st.sidebar.slider("Price Range", price_min, price_max)

# Filtro de livros por preço.
slider_price = df_top100_books[df_top100_books["book price"] <= price]
slider_price

# Gráficos.
fig = px.bar(df_top100_books["year of publication"].value_counts(), title="Livros por Ano")
fig_2 = px.histogram(df_top100_books["book price"], title ="Distribuição de preços.")
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig_2)