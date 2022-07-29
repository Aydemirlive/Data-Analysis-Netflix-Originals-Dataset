from datetime import date
import datetime
from turtle import color
from typing_extensions import runtime
from matplotlib import style
from matplotlib.pyplot import scatter
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px
import seaborn as sns

data = pd.read_csv("NetflixOriginals.csv",encoding='ISO-8859-1')
                #The Longest Film Language
longfilm=data[(data['Runtime']>90) & (data['Language'])]
bar =px.bar(longfilm,x="Language",y="Runtime")
bar.show()
                #The IMDB Score Documentary Genre between 2019 January and 2020 June
data['Premiere'] = pd.to_datetime(data.Premiere)
docimdb=data[(data['Genre']=='Documentary') & ((data['Premiere']>'2019-01-01') & (data['Premiere']<'2020-06-01')) & (data['IMDB Score'])]
scatter= px.scatter(docimdb,x="Premiere",y="IMDB Score")
scatter.show()
                #Highest IMDB Score of English Fİlms
mostratingEnglish=data[(data['Language']=='English')]
print(mostratingEnglish.sort_values(by="IMDB Score",axis=0,ascending=False).head(1))
                #The Films of Hindi Language
hindifilms=data[(data['Language']=='Hindi')]
print(hindifilms['Runtime'].mean())
                #The Category of Genre Column
print(data['Genre'].value_counts()) 
genre=data['Genre'].value_counts()
fig=px.bar(data['Genre'],x='Genre',y=genre)
fig.show()
                #The most used Language
print(data['Language'].value_counts().head(3))

                #The Films of Highest IMDB Score
print(data[['Title','IMDB Score']].sort_values(by='IMDB Score',axis=0,ascending=False).head(10))
                #The Corelation Between IMDB Score and Runtime
korelasyon =data[['IMDB Score','Runtime']] 
print(korelasyon.corr())
fig=sns.heatmap(korelasyon.corr())
fig.show()

            #The Genre has highest IMSB Score
print((data.groupby('Genre')['IMDB Score'].apply(lambda x: np.mean(x)).sort_values(axis=0,ascending=False).head(10)))
updateddata=data.groupby('Genre')['IMDB Score'].apply(lambda x: np.mean(x)).sort_values(axis=0,ascending=False).head(10).reset_index()
fig=px.line(x=updateddata["Genre"],y=updateddata["IMDB Score"])
fig.show()

            #The Films of longest Runtime
print(data[['Runtime','Title']].sort_values(by='Runtime',axis=0,ascending=False).head(10))
runtimedata=data[['Runtime','Title']].sort_values(by='Runtime',axis=0,ascending=False).head(10)
fig=px.bar(runtimedata,x="Title",y="Runtime")
fig.show()

            #The year has most films
print(data['Premiere'].value_counts())
            #The Language has lowest IMDB Score
print((data.groupby('Language')['IMDB Score'].apply(lambda x: np.mean(x)).sort_values(axis=0,ascending=True).head(5)))

            # The year has the greatest total runtime
print(data.groupby("Year")["Runtime"].apply(lambda x: np.mean(x)).sort_values(by="Runtime", ascending=False).head(1))   

            # The most used "Genre" of each language
print(data.groupby("Language")["Genre"].value_counts(sort=True).head(1))

            