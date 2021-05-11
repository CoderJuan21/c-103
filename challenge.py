import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")

fig = px.bar(df, x = "Country", y = "Per capita income")
fig.show()