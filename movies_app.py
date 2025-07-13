import streamlit as st
import pandas as pd
import pickle
import requests


# Load pickle file.
movies_dict = pickle.load(open('movie_dict.pkl', 'rb')) # Load pickle file
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# fectch image link. or poster link.
def fetch_poster(movie_id):
    api_key = 'Your API  Key'  # Replace with your actual OMDb API key
    url = f'https://www.omdbapi.com/?i={movie_id}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Poster'] # extracting Poster from json file. Poster containing image link.


# Function for recommendation
def recommendation(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['imdb_id']
        recommended_movies.append(movies.iloc[i[0]]['title'])
        # fetch poster via API
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters



# Add Title
st.title('Movie Recommendation System')



# inserted select box for movies list.
selected_movie_name = st.selectbox(
    'Select Movies from given list',
    movies['title'].values
)



# insert button
if st.button('Recommend'):
    names, posters = recommendation(selected_movie_name) # we can also run loop here to reduce code redundancy.
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


print(movies.columns.tolist())
