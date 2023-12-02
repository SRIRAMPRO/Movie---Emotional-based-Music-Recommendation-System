import streamlit as st
from PIL import Image
import json
from Classifier import KNearestNeighbours
from bs4 import BeautifulSoup
import requests, io
from urllib.request import urlopen
import PIL.Image
from urllib.request import urlopen

with open('./Data/movie_data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open('./Data/movie_titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)
hdr = {'User-Agent': 'Mozilla/5.0'}


st.set_page_config(layout="wide")


#st.set_page_config(layout="wide")

def movie_poster_fetcher(imdb_link):
    # Fetch IMDb page
    url_data = requests.get(imdb_link, headers=hdr).text
    s_data = BeautifulSoup(url_data, 'html.parser')
    
    # Find the meta tag containing the poster image URL
    imdb_dp = s_data.find("meta", property="og:image")
    
    if imdb_dp:
        movie_poster_link = imdb_dp.attrs['content']
        u = urlopen(movie_poster_link)
        raw_data = u.read()
        image = PIL.Image.open(io.BytesIO(raw_data))
        image = image.resize((300, 600), )
        st.image(image, use_column_width=False)
    else:
        st.warning("Poster not found for this movie.")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


st.markdown("<h1 style='text-align: center; font-size: 48px;'>Nexus</h1>", unsafe_allow_html=True)

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(299534),  # Avengers: Endgame (Marvel)
    fetch_poster(284054),  # Black Panther (Marvel)
    fetch_poster(429617),  # Spider-Man: Far From Home (Marvel)
    fetch_poster(118340),  # Guardians of the Galaxy (Marvel)
    fetch_poster(1726),    # Iron Man (Marvel)
    fetch_poster(155),     # The Dark Knight (DC)
    fetch_poster(297762),  # Wonder Woman (DC)
    fetch_poster(297802),  # Aquaman (DC)
    fetch_poster(49521),   # Man of Steel (DC)
    fetch_poster(297761),  # Suicide Squad (DC)
    fetch_poster(285),     # Pirates of the Caribbean: The Curse of the Black Pearl
    fetch_poster(1865),    # Pirates of the Caribbean: Dead Man's Chest
    fetch_poster(258),     # Pirates of the Caribbean: At World's End
    fetch_poster(166426),  # Pirates of the Caribbean: Dead Men Tell No Tales
    fetch_poster(24428),   # The Avengers
    fetch_poster(76338),   # The Avengers: Age of Ultron
    fetch_poster(284052),  # Avengers: Infinity War
    fetch_poster(299536),  # Avengers: Endgame
    fetch_poster(320288),  # Spider-Man: Homecoming
    fetch_poster(447404),  # Spider-Man: No Way Home
    fetch_poster(181808),  # Star Wars: The Last Jedi
    fetch_poster(671),     # Harry Potter and the Philosopher's Stone
    fetch_poster(672),     # Harry Potter and the Chamber of Secrets
    fetch_poster(674),     # Harry Potter and the Prisoner of Azkaban
    fetch_poster(673),     # Harry Potter and the Goblet of Fire
    fetch_poster(675),     # Harry Potter and the Order of the Phoenix
    fetch_poster(121),     # Harry Potter and the Half-Blood Prince
    fetch_poster(767),     # Harry Potter and the Deathly Hallows: Part 1
    fetch_poster(12445),   # Harry Potter and the Deathly Hallows: Part 2
    fetch_poster(157336),  # Interstellar
    fetch_poster(27205),   # Inception
    fetch_poster(680),     # Inception
    fetch_poster(680),     # Jurassic Park
    fetch_poster(672),     # Jurassic Park
    fetch_poster(12),      # Finding Nemo
    fetch_poster(13),      # Toy Story
    fetch_poster(862),     # Toy Story
    fetch_poster(278),     # The Shawshank Redemption
    fetch_poster(238),     # The Godfather
    fetch_poster(424),     # Schindler's List
    fetch_poster(858),     # The Big Lebowski
    fetch_poster(550),     # Fight Club
    fetch_poster(550),     # The Matrix
    fetch_poster(77),      # Gladiator
    fetch_poster(38),      # Django Unchained
    fetch_poster(8587),    # The Grand Budapest Hotel
    fetch_poster(114),     # Inglourious Basterds
    fetch_poster(862),     # Toy Story 2
    fetch_poster(78),      # Inception
    fetch_poster(510),     # The Lion King
    fetch_poster(562),     # A Beautiful Mind
    fetch_poster(1891),    # The Lion King
    fetch_poster(807),     # Se7en
    fetch_poster(268896),  # Bambi
    fetch_poster(135397),  # Jurassic World
    fetch_poster(405),     # Inside Out
    fetch_poster(389),     # 12 Angry Men
    fetch_poster(17204),   # Shutter Island
    fetch_poster(109),     # 10 Things I Hate About You
    fetch_poster(146),     # The Exorcist
    fetch_poster(240),     # The Godfather: Part II
    fetch_poster(290),     # Scarface
    fetch_poster(105),     # Back to the Future
    fetch_poster(128),     # Spirited Away
    fetch_poster(568),     # Fargo
    fetch_poster(387),     # Goodfellas
    fetch_poster(577),     # Life Is Beautiful
    fetch_poster(78),      # The Shining
    fetch_poster(238),     # Pulp Fiction
    fetch_poster(10138),   # Jurassic Park III
    fetch_poster(101299),  # Anchorman: The Legend of Ron Burgundy
    fetch_poster(607),     # Men in Black
    fetch_poster(652),     # Tangled
    fetch_poster(755),     # Wedding Crashers
    fetch_poster(121),     # Harry Potter and the Philosopher's Stone
    fetch_poster(767),     # Harry Potter and the Deathly Hallows: Part 1
    fetch_poster(122),     # The Lord of the Rings: The Fellowship of the Ring
    fetch_poster(155),     # The Dark Knight
    fetch_poster(272),     # Batman Begins
    fetch_poster(763),     # The Lord of the Rings: The Return of the King
    fetch_poster(671),     # Harry Potter and the Philosopher's Stone
    fetch_poster(672),     # Harry Potter and the Chamber of Secrets
    fetch_poster(11324),   # Spirited Away
    fetch_poster(1422),    # The Lord of the Rings: The Two Towers
    fetch_poster(769),     # Up
    fetch_poster(77338),   # How to Train Your Dragon
    fetch_poster(8358),    # Ratatouille
    fetch_poster(297),     # Toy Story 3
    fetch_poster(138),     # WALL·E
    fetch_poster(664),     # Monsters, Inc.
    fetch_poster(857),     # Finding Nemo
    fetch_poster(180),     # The Incredibles
    fetch_poster(185),     # Ratatouille
    fetch_poster(22),      # WALL·E
    fetch_poster(103),     # Up
    fetch_poster(226),     # Toy Story 3
    fetch_poster(55),      # The Lion King
    fetch_poster(85),      # Forrest Gump
    fetch_poster(680),     # Inception
    fetch_poster(77),      # Gladiator
    fetch_poster(497),     # Pirates of the Caribbean: The Curse of the Black Pearl
    fetch_poster(664),     # The Pursuit of Happyness
    fetch_poster(857),     # Avatar
    fetch_poster(180),     # The Incredibles
    fetch_poster(185),     # Ratatouille
    fetch_poster(22),      # WALL·E
    fetch_poster(103),     # Up
    fetch_poster(226),     # Toy Story 3


]


imageCarouselComponent(imageUrls=imageUrls, height=200)

def get_movie_info(url):
 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        
        movie_title = soup.find('meta', property='og:title')['content'].split(' (')[0]

        
        rating_and_genres = soup.find('meta', property='og:title')['content'].split('⭐')[1].strip()
        imdb_rating = rating_and_genres.split('|')[0].strip()
        genres = rating_and_genres.split('|')[1].strip()

       
        movie_description = soup.find('meta', attrs={'name': 'description'})['content']

        return movie_title, imdb_rating, genres, movie_description

def KNN_Movie_Recommender(test_point, k):
    
    target = [0 for item in movie_titles]
    model = KNearestNeighbours(data, target, test_point, k=k)
    model.fit()
    table = []
    for i in model.indices:
        table.append([movie_titles[i][0], movie_titles[i][2], data[i][-1]])
    print(table)
    return table


#st.markdown("<h1 style='text-align: center; font-size: 48px;'>Nexus</h1>", unsafe_allow_html=True)


def run():

    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Get Your Favourate Movies Here"</h4>''',
                unsafe_allow_html=True)
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    movies = [title[0] for title in movie_titles]
    category = ['--Select--', 'Movie based', 'Genre based']
    cat_op = st.selectbox('Select Recommendation Type', category)
    if cat_op == category[0]:
        st.warning('Please select Recommendation Type!!')
    elif cat_op == category[1]:
        select_movie = st.selectbox('Select movie: (Recommendation will be based on this selection)',
                                    ['--Select--'] + movies)
        dec = st.radio("Want to Fetch Movie Poster?", ('Yes', 'No'))
        st.markdown(
            '''<h4 style='text-align: left; color: #d73b5c;'>* How Many Movies You Want!!"</h4>''',
            unsafe_allow_html=True)
        if dec == 'No':
            if select_movie == '--Select--':
                st.warning('Please select Movie!!')
            else:
                no_of_reco = st.slider('Number of movies you want Recommended:', min_value=5, max_value=20, step=1)
                genres = data[movies.index(select_movie)]
                test_points = genres
                table = KNN_Movie_Recommender(test_points, no_of_reco + 1)
                table.pop(0)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                for movie, link, ratings in table:
                    c += 1
                    director, cast, story, total_rat = get_movie_info(link)
                    st.markdown(f"({c})[ {movie}]({link})")
                    st.markdown('Movie Name: '+str(director))
                    #st.markdown('Year: '+str(cast))
                    st.markdown('Genere: '+str(story))
                    st.markdown('Movie Description: '+str(total_rat))
                    st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
        else:
            if select_movie == '--Select--':
                st.warning('Please select Movie!!')
            else:
                no_of_reco = st.slider('Number of movies you want Recommended:', min_value=5, max_value=20, step=1)
                genres = data[movies.index(select_movie)]
                test_points = genres
                table = KNN_Movie_Recommender(test_points, no_of_reco + 1)
                table.pop(0)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                for movie, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {movie}]({link})")
                    movie_poster_fetcher(link)
                    director, cast, story, total_rat = get_movie_info(link)
                    st.markdown(director)
                    #st.markdown(cast)
                    st.markdown(story)
                    st.markdown(total_rat)
                    st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
    elif cat_op == category[2]:
        sel_gen = st.multiselect('Select Genres:', genres)
        dec = st.radio("Want to Fetch Movie Poster?", ('Yes', 'No'))
        st.markdown(
            '''<h4 style='text-align: left; color: #d73b5c;'>*You have a Awesome Movie Taste!!"</h4>''',
            unsafe_allow_html=True)
        if dec == 'No':
            if sel_gen:
                imdb_score = st.slider('Choose IMDb score:', 1, 10, 8)
                no_of_reco = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(imdb_score)
                table = KNN_Movie_Recommender(test_point, no_of_reco)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                for movie, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {movie}]({link})")
                    director, cast, story, total_rat = get_movie_info(link)
                    st.markdown(director)
                    #st.markdown(cast)
                    st.markdown(story)
                    st.markdown(total_rat)
                    st.markdown('IMDB Rating: ' + str(ratings) + '⭐')
        else:
            if sel_gen:
                imdb_score = st.slider('Choose IMDb score:', 1, 10, 8)
                no_of_reco = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(imdb_score)
                table = KNN_Movie_Recommender(test_point, no_of_reco)
                c = 0
                st.success('Some of the movies from our Recommendation, have a look below')
                for movie, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {movie}]({link})")
                    movie_poster_fetcher(link)
                    director, cast, story, total_rat = get_movie_info(link)
                    st.markdown(director)
                    #st.markdown(cast)
                    st.markdown(story)
                    st.markdown(total_rat)
                    st.markdown('IMDB Rating: ' + str(ratings) + '⭐')


run()
