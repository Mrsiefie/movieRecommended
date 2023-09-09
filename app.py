import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movie[movie['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list =sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movie =[]
    for i in movie_list:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
st.title('Movie Recommended System')

 similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name= st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    recomdation = recommend(selected_movie_name)
    for i in recomdation:
        st.write(i)
