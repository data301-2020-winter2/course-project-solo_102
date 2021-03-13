import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Load data

    dogs_raw = pd.read_csv(url_or_path_to_csv_file)

    # Drop unwanted columns, rename columns, remove outliers, reset index

    dogs = (dogs_raw.drop(columns=['name', 'housebroken', 'likes_people', 'likes_children', 'get_along_males', 'get_along_females', 'get_along_cats', 'keep_in'])
                    .rename(columns={'coat':'coat_length'})
                    .rename(columns={'posted':'date_posted'})
                    .drop(dogs_raw[dogs_raw['age']>15].index)
                    .reset_index()
                    .drop(columns=['index']))

    # set datetime data

    dogs['date_found'] = pd.to_datetime(dogs['date_found'])
    dogs['adoptable_from'] = pd.to_datetime(dogs['adoptable_from'])
    dogs['date_posted'] = pd.to_datetime(dogs['date_posted'])

    # create new columns

    dogs = (dogs.assign(month_found = dogs['date_found'].dt.month)
                .assign(year_found = dogs['date_found'].dt.year))

    return dogs

