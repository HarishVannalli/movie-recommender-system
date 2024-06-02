

# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# # Function to fetch movie poster from OMDb
# def fetch_poster(movie_title):
#     url = f'https://www.omdbapi.com/?t={movie_title}&apikey=bc7209bd'
#     response = requests.get(url)
#     data = response.json()
#     return data['Poster']
#
# # Function to recommend movies
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_title = movies.iloc[i[0]].title
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_title))
#     return recommended_movies, recommended_movies_posters
#
# # Load movie data
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# # Load similarity data
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Streamlit app
# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)
#
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])


import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie poster from OMDb
def fetch_poster(movie_title):
    url = f'https://www.omdbapi.com/?t={movie_title}&apikey=bc7209bd'
    response = requests.get(url)
    data = response.json()
    return data['Poster']

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_movies_posters

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity data
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
# st.title('Movie Recommender System')

# Center-align the title
st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])





