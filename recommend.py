import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pd.read_csv('./movies1.csv', sep=',', encoding='latin-1', usecols=['movie_id', 'title', 'genres'], engine='python')

movies['genres'] = movies['genres'].str.split('|')
movies['genres'] = movies['genres'].fillna("").astype('str')

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(movies['genres'])

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

titles = movies['title']
mlid = movies['movie_id']
indices = pd.Series(movies.index, index=movies['title'])

def rec(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    temp=(mlid.iloc[movie_indices]).to_numpy()
    return temp.tolist()

print(rec(sys.argv[1]))