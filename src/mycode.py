import pandas as pd

df = pd.read_csv("data/sample.csv")
df.loc[len(df)] = ["Asha", 29, "Chennai"]
df.to_csv("data/sample.csv", index=False)
print("Added new row to dataset!")