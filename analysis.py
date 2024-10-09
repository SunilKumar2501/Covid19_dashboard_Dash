import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

patients = pd.read_csv("IndividualDetails.csv")
total = patients.shape[0]
active = patients[patients["current_status"] == "Hospitalized"].shape[0]
recovered = patients[patients["current_status"] == "Recovered"].shape[0]
deaths = patients[patients["current_status"] == "Deceased"].shape[0]

p_bar = patients["detected_state"].value_counts().reset_index()
print(p_bar)

p_bar = patients[patients["current_status"] == "Hospitalized"].value_counts().reset_index()
print(p_bar)

p_bar = patients["detected_state"].value_counts().reset_index()
print(p_bar)

p_bar = patients["detected_state"].value_counts().reset_index()
print(p_bar)


