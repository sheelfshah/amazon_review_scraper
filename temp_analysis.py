import pandas as pd
import numpy as np

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

rating = df["rating"].to_numpy()
num_revs = 0
tot_rat = 0
for i in range(rating.shape[0]):
    if rating[i] < 5:
        num_revs += 1
        tot_rat += rating[i]

print(tot_rat / num_revs, num_revs, rating.shape[0])
