import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data1.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.bar(mean, x="student_id", y = "level",  color="attempt", orientation="h")
fig.show()