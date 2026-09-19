"""
Video Game Sales Analytics — 40 Years of Gaming Industry Data
A comprehensive video game industry analytics project examining sales of over 16,500 titles across four decades, highlighting platform dominance, genre shifts, and regional consumer behavior.

Original Kaggle Notebook: https://www.kaggle.com/code/lazer999/video-game-sales-analysis-for-gamers
Author: Muhammad Musa Khan (Kaggle Master: https://kaggle.com/lazer999)
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

# --- Smart Dataset Path Resolution ---
def _resolve_data_path(file_path):
    """Checks local and data/ directories if dataset path is missing."""
    if os.path.exists(file_path):
        return file_path
    base = os.path.basename(file_path)
    candidates = [
        base,
        os.path.join("data", base),
        os.path.join("..", "data", base),
        file_path.replace("/kaggle/input/", "data/"),
        file_path.replace("../input/", "data/"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return file_path

# --- Pipeline Execution ---

# --- Cell 1 ---
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import plotly.express as px
print("Setup Complete") 

# --- Cell 2 ---
sns.set_style('darkgrid')
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (9, 5)
plt.rcParams['figure.facecolor'] = '#00000000'

# --- Cell 3 ---
df=pd.read_csv('../input/videogamesales/vgsales.csv')

# --- Cell 4 ---
df.head()

# --- Cell 5 ---
df.shape

# --- Cell 6 ---
df.describe()

# --- Cell 7 ---
df.info()

# --- Cell 8 ---
#checking for null values
df.isnull().sum()

# --- Cell 9 ---
#dropping null values
df.dropna(inplace=True)

# --- Cell 10 ---
df.head()

# --- Cell 11 ---
sns.heatmap(df.corr(), annot=True);
#There isn't much to see here. Sales are directly co-related to sales.

# --- Cell 12 ---
df['Genre'].unique()

# --- Cell 13 ---
df["Platform"].unique()

# --- Cell 14 ---
df['Year'].unique()


# --- Cell 15 ---
df[df['Year'].isin([2017,2018,2019,2020])]

# --- Cell 16 ---
df.drop(df[df['Year'].isin([2017,2018,2019,2020])].index,inplace=True)

# --- Cell 17 ---
df.sort_values(by='Global_Sales',ascending=False).head(10)

# --- Cell 18 ---
sns.barplot(y=df.Name.head(10),x=df.Global_Sales.head(10));
plt.title("Top Selling Games");

# --- Cell 19 ---
sales_per_year=df.groupby('Year')['Global_Sales'].sum()

# --- Cell 20 ---
sales_per_year

# --- Cell 21 ---
sns.lineplot(y=sales_per_year,x=sales_per_year.index)
plt.title("Sales over the years")
plt.ylabel("Sales")

# --- Cell 22 ---
genre_sales=df.groupby(["Genre"])["Global_Sales"].sum().sort_values(ascending=False)

# --- Cell 23 ---
genre_sales

# --- Cell 24 ---
data=genre_sales
labels=[]
for x in genre_sales.index:
    labels.append(x)

# --- Cell 25 ---
plt.figure(figsize=(12,6))
sns.barplot(x=genre_sales.index,y=genre_sales)
plt.ylabel("Sales")
plt.title("Genre Sales")
plt.xticks(rotation=45);

# --- Cell 26 ---
#colors = sns.color_palette('pastel')[0:12]
plt.pie(data,labels=labels, autopct='%.0f%%')
plt.figure(figsize=(12,7))
plt.show();

# --- Cell 27 ---
Top_platforms=df.groupby(["Platform"])["Global_Sales"].sum().sort_values(ascending=False).head(10)

# --- Cell 28 ---
plt.figure(figsize=(12,6))
sns.barplot(x=Top_platforms.index,y=Top_platforms)
plt.ylabel("Sales")
plt.title("Platforms");

# --- Cell 29 ---
plt.pie(Top_platforms,labels=Top_platforms.index, autopct='%.0f%%');
plt.figure(figsize=(12,7));

# --- Cell 30 ---
Top_Games_perY=df[df.groupby("Year")["Global_Sales"].transform(max)==df['Global_Sales']]
Top_Games_perY=Top_Games_perY.set_index('Year').sort_values(by="Year")
Top_Games_perY

# --- Cell 31 ---
df.groupby(['Genre','Platform'])["Global_Sales"].mean().sort_values(ascending=False).head(10)

# --- Cell 32 ---
# Melt the DataFrame
games_melted = pd.melt(df, 
                       id_vars=['Name',"Year"], 
                       value_vars=['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales'], 
                       var_name='Region', 
                       value_name='Sales')

# Now we can graph our boxplot
sns.boxplot(x='Region', y='Sales', data=games_melted, palette='rocket', showfliers=False)
sns.despine()

# --- Cell 33 ---
over_year=df.groupby(['Year'])['NA_Sales','JP_Sales','EU_Sales','Other_Sales'].sum()

# --- Cell 34 ---
over_year.plot()
plt.title("Trend of sales over Regions")
plt.ylabel("Sales");

# --- Cell 35 ---
#sns.histplot(data=df,x="Year",bins=36)
#plt.figure(figsize=(16,9))
fig=px.histogram(df,
                 x='Year',
                 marginal='box',
                 color_discrete_sequence=['Green'],
                 title="Games count")
fig.update_layout(bargap=0.1)
fig.show()

# --- Cell 36 ---
df['Year'].value_counts().head()

# --- Cell 37 ---
df['Year'].value_counts().tail()



if __name__ == "__main__":
    print("Pipeline execution complete.")
