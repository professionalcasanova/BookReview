import streamlit as st
import pandas as pd

# Carregar arquivos (Datasets)
df_reviews = pd.read_csv("CaminhoDoDiretorio/customer reviews.csv")
df_top100_books = pd.read_csv("CaminhoDoDiretorio/Top-100 Trending Books.csv")

# Selecionar um livro da lista.
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

# Filtrar informações do livro selecionado.
dfBooks = df_top100_books[df_top100_books["book title"] == book]
dfReviews = df_reviews[df_reviews["book name"] == book]

# Exibir detalhes do livro.
if not dfBooks.empty:
    st.title(dfBooks["book title"].iloc[0])
    st.subheader(dfBooks["genre"].iloc[0])

    col1, col2, col3 = st.columns(3)
    col1.metric("Price", f"${dfBooks['book price'].iloc[0]}")
    col2.metric("Rating", dfBooks["rating"].iloc[0])
    col3.metric("Year", dfBooks["year of publication"].iloc[0])

    st.divider()
    st.subheader("Reviews")

    # Exibir avaliações
    for _, row in dfReviews.iterrows():
        message = st.chat_message(row['reviewer'])
        message.write(f"**Review:** {row['review title']}")
        message.write(row['review description'])
