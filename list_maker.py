import pandas as pd

test = pd.read_csv("test.csv").as_matrix()

print(len(test))

print(test[0])