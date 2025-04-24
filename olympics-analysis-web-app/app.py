import streamlit as st
import pandas as pd
import preprocessor
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")

st.sidebar.title('Olympics Analysis')

df = preprocessor.preprocess(df,region_df)

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis')
)


if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years,country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title("OVERALL TALLY")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title(" MEDAL TALLY IN "+ str(selected_year).upper() + " OLYMPICS ")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country.upper() + " OVERALL PERFORMANCE ")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country.upper() + " PERFORMANCE IN "+ str(selected_year).upper() + " OLYMPICS ")
    st.table(medal_tally)



if user_menu == 'Overall Analysis':
    st.title("TOP STATISTICS")
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)

    st.title('PARTICIPATING NATIONS OVER YEARS')
    nations_over_time = helper.participating_nations_over_time(df)
    fig = px.line(nations_over_time, x="Year", y="Count")
    st.plotly_chart(fig)
    st.title('EVENTS OVER YEARS')
    events_over_time = helper.events_over_time(df)
    fig1 = px.line(events_over_time, x="Year", y="Events")
    st.plotly_chart(fig1)
    st.title('ATHLETES OVER YEARS')
    athletes_over_time = helper.athletes_over_time(df)
    fig2 = px.line(athletes_over_time, x="Year", y="Names")
    st.plotly_chart(fig2)

    st.title('NUMBER OF EVENTS OVER TIME')
    fig, ax = plt.subplots(figsize=(35, 30))
    x = df.drop_duplicates(subset=['Year', 'Sport', 'Event'])
    heatmap_data = x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int)
    sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)

    st.title('MOST SUCCESSFUL ATHLETES')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)


if user_menu == 'Country-wise Analysis':
    st.title('COUNTRY-WISE ANALYSIS')
    country_list =  df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.selectbox('Select a Country',country_list)
    country_df = helper.year_wise_medal_tally(df,selected_country)
    fig = px.line(country_df,x='Year',y='Medal')
    st.title(selected_country.upper()+' Medal Tally the Years')
    st.plotly_chart(fig)
    st.title(selected_country.upper() + ' excels in following sports')
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(35, 30))
    if not pt.empty:
        sns.heatmap(pt, annot=True, ax=ax)
    else:
        ax.text(0.5, 0.5, "No Data Available", ha="center", va="center", fontsize=20)
        ax.set_xticks([])
        ax.set_yticks([])
    st.pyplot(fig)
