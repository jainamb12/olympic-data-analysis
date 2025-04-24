import numpy as np
import pandas as pd

temp_df = pd.DataFrame()
def medal_tally(df):
    medal_tally1 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally1 = medal_tally1.groupby('NOC').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
    ascending=False).reset_index()
    medal_tally1['total'] = medal_tally1['Gold'] + medal_tally1['Silver'] + medal_tally1['Bronze']
    return medal_tally1

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'overall')
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'overall')
    return years,country


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    global temp_df
    # Convert 'Overall' to lowercase for consistency
    year = str(year).lower()
    country = str(country).lower()
    if year == 'overall' and country == 'overall':
        temp_df = medal_df
    elif year == 'overall' and country != 'overall':
        flag = 1
        temp_df = medal_df[medal_df['region'].str.lower() == country]
    elif year != 'overall' and country == 'overall':
        if year.isnumeric():  # Ensure it is a number before conversion
            temp_df = medal_df[medal_df['Year'] == int(year)]
        else:
            return None  # Handle cases where year is not a number
    elif year != 'overall' and country != 'overall':
        if year.isnumeric():  # Ensure it's a number
            temp_df = medal_df[(medal_df['region'].str.lower() == country) & (medal_df['Year'] == int(year))]
        else:
            return None
    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year', ascending=True).reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold', ascending=False).reset_index()
    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x

def participating_nations_over_time(df):
    nations_over_time = df.drop_duplicates(subset=['Year', 'region']).groupby('Year').size().reset_index(
        name='Count').sort_values('Year')
    return nations_over_time

def events_over_time(df):
    event_over_time = df.drop_duplicates(subset=['Year', 'Event']).groupby('Year').size().reset_index(name='Events').sort_values('Year')
    return event_over_time

def athletes_over_time(df):
    athlete_over_time = df.drop_duplicates(subset=['Year', 'Name']).groupby('Year').size().reset_index(
        name='Names').sort_values('Year')
    return athlete_over_time

def most_successful(df, sport):
    global temp_df
    temp_df = df.dropna(subset=['Medal'])
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    medal_counts = temp_df['Name'].value_counts().reset_index()
    medal_counts.columns = ['Name', 'Medals']
    x = (medal_counts.head(15).merge(df[['Name', 'Sport', 'region']], on='Name', how='left').drop_duplicates('Name'))
    return x

def year_wise_medal_tally(df,country):
    global temp_df
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df

def country_event_heatmap(df,country):
    global temp_df
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt