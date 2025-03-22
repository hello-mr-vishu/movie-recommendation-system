import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x: x[1])[1:6]
    
    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

with open('movie_dict.pkl', 'rb') as file:  
    movies_dict = pickle.load(file)

with open('similarity.pkl', 'rb') as file:  
    similarity = pickle.load(file)

movies = pd.DataFrame(movies_dict)
st.title('Movie Recommeder System')


selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommed'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)