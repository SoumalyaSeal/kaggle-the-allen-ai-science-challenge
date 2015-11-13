import pandas as pd


test = pd.read_csv("../data/original/validation_set.tsv", sep='\t')

test.to_csv("../data/prepped/test.csv")
