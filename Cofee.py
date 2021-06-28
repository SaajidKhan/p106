import pandas as pd
import plotly.express as px
import csv

with open("Cofee.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="week",y="Coffee in ml")
    fig.show()
