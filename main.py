import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

###### helper functions. Use them when needed #######
def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]
##################################################

# Step 1: Read CSV File
df = pd.read_csv("tv_shows_dataset.csv")
# print(df.columns)

# Step 2: Select Features
features = ['Genre']
features
for feature in features:
	df[feature] = df[feature].fillna('')
