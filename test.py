import pandas as pd

df = pd.read_excel('dataset.xlsx')


# test each columns how much null values are exist 


null_counts = df.isna().sum()

# print(null_counts)

null_percents = null_counts / len(df)

# print(null_percents)

columns_to_drop = null_percents[null_percents > 0.8].index
print("before:" , len(df.columns))
df = df.drop(columns=columns_to_drop)

print("after",len(df.columns))