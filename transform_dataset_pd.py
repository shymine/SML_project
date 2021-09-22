import os
import tqdm

path = "datasets/polarity_datasetV2/txt_sentoken"

# shape of examples: "review", "pos" (1 if True, 0 if False)
examples = []
neg_review = [path+"/neg/"+f for f in os.listdir(path+"/neg")]
pos_review = [path+"/pos/"+f for f in os.listdir(path+"/pos")]
for review in tqdm.tqdm(neg_review):
    with open(review, 'r') as r:
        examples.append({"review":r.read(), "pos":0})
for review in tqdm.tqdm(pos_review):
    with open(review, 'r') as r:
        examples.append({"review":r.read(), "pos":1})

import pandas as pd

df = pd.DataFrame(examples)

df.to_csv("polarity_dataframe.csv")