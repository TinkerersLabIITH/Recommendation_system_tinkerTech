import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pickled data
popular_df = pickle.load(open('model/popular.pkl','rb'))
pt = pickle.load(open('model/pt.pkl','rb'))
books = pickle.load(open('model/books.pkl','rb'))
similarity_scores = pickle.load(open('model/similarity_scores.pkl','rb'))

# Streamlit app
st.set_page_config(page_title="Book Recommender System", layout="wide")
st.title("📚 Book Recommender System")

# --- Home Page (Popular Books) ---
st.subheader("🔥 Top Popular Books")
cols = st.columns(5)  # display in grid format
for i, col in enumerate(cols):
    with col:
        if i < len(popular_df):
            st.image(popular_df['Image-URL-M'].values[i], width=120)
            st.markdown(f"*{popular_df['Book-Title'].values[i]}*")
            st.caption(popular_df['Book-Author'].values[i])
            st.write(f"⭐ {round(popular_df['avg_rating'].values[i],2)} | 🗳 {popular_df['num_ratings'].values[i]} votes")

# --- Recommendation Section ---
st.subheader("🔍 Find Similar Books")

user_input = st.selectbox(
    "Search by book name",
    pt.index.values
)

if st.button("Recommend"):
    try:
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        st.write("### Recommended Books for You:")
        rec_cols = st.columns(4)

        for i, col in zip(similar_items, rec_cols):
            temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')

            book_title = temp_df['Book-Title'].values[0]
            book_author = temp_df['Book-Author'].values[0]
            book_image = temp_df['Image-URL-M'].values[0]

            with col:
                st.image(book_image, width=130)
                st.markdown(f"*{book_title}*")
                st.caption(book_author)

    except Exception as e:
        st.error("Book not found in the dataset. Please try another one.")