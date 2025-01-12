import streamlit as st
import pickle
import pandas as pd
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie recommender system")
selected_movie = st.selectbox(
    "Select any movie",
    movies['title'].values)
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for recom_movies in recommendations:
        st.write(recom_movies)