import pandas as pd
import streamlit as st
import pickle
import requests

tv_shows_dict = pickle.load(open('tv_shows_dict.pkl','rb'))
tv_shows = pd.DataFrame(tv_shows_dict)
cosine_similarity = pickle.load(open('cosine_similarity.pkl','rb'))

st.header('TV Show Recommender System')

selected_tv_show_name = st.selectbox(
'Choose that one TV show that is your all time favourite!',
tv_shows['title'].values)
# print(type(selected_tv_show_name))

def fetch_poster(tv_show_name):
    s = tv_show_name
    s1 = s.replace(" ", "+")
    url = "https://api.themoviedb.org/3/search/tv?api_key=3122717ed8290a2d358df8985cc89216&query={}".format(s1)
    data = requests.get(url)
    data = data.json()
    # print(data)
    # print(type(data))
    poster_path = data['results'][0]['poster_path']
    # print(poster_path)
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # print(full_path)
    return full_path

# fetch_poster(selected_tv_show_name)
st.image(fetch_poster(selected_tv_show_name), width=200)

# the function takes a tv_show and returns 10 recommended tv_shows
def recommend(tv_show):
    tv_show_index = tv_shows[tv_shows['title'] == tv_show].index[0]
    distances = cosine_similarity[tv_show_index]
    tv_shows_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    # sort_by_IMDB = sorted(tv_shows_list, key=lambda x:tv_shows["IMDB Rating"][x[0]],reverse=True)

    recommended_tv_show_posters = []
    recommended_tv_shows = []

    for i in tv_shows_list[1:11]:
        recommended_tv_shows.append(tv_shows.iloc[i[0]].title)
    return recommended_tv_shows


if st.button('Recommend'):
    recommendations = recommend(selected_tv_show_name)
    posters = recommend(selected_tv_show_name)
    # print(recommendations)

    st.write("People also search for:")

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        pic0 = posters[0]
        st.image(fetch_poster(pic0), width=150)
    with col2:
        st.text(recommendations[1])
        pic1 = posters[1]
        st.image(fetch_poster(pic1), width=150)
    with col3:
        st.text(recommendations[2])
        pic2 = posters[2]
        st.image(fetch_poster(pic2), width=150)
    with col4:
        st.text(recommendations[3])
        pic3 = posters[3]
        st.image(fetch_poster(pic3), width=150)
    with col5:
        st.text(recommendations[4])
        pic4 = posters[4]
        st.image(fetch_poster(pic4), width=150)
    with col6:
        st.text(recommendations[5])
        pic5 = posters[5]
        st.image(fetch_poster(pic5), width=150)
    with col7:
        st.text(recommendations[6])
        pic6 = posters[6]
        st.image(fetch_poster(pic6), width=150)
    with col8:
        st.text(recommendations[7])
        pic7 = posters[7]
        st.image(fetch_poster(pic7), width=150)
    with col9:
        st.text(recommendations[8])
        pic8 = posters[8]
        st.image(fetch_poster(pic8), width=150)
    with col10:
        st.text(recommendations[9])
        pic9 = posters[9]
        st.image(fetch_poster(pic9), width=150)

    # for i in recommendations:
    #     st.write(i)
        # st.image(fetch_poster(i))