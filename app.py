import streamlit as st
import pickle
import requests


st.title('Movies Recommender System')
movies=pickle.load(open('movies.pkl', 'rb'))
movies_list=movies['title'].values
selected_movie=st.selectbox('Select an option',movies_list)

similarity=pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster (movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3e9f9c23a4d6835c0a49a5c0440ceedb&language=en-US'
.format(movie_id))
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster



if st.button('Recommend') :
    name,poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])




