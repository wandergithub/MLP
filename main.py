import pandas as pd
# read data
df = pd.read_csv('./data/anime_info.dat', delimiter='\t')
# Remove entries
index = df[df['genre'].fillna('').str.contains('Hentai')].index
df = df.drop(index)


print(df.head(20))