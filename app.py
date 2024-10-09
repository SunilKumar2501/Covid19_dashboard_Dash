import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# External CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknl.PMO',
        'crossorigin': 'anonymous'
    }
]

patients = pd.read_csv("IndividualDetails.csv")
total = patients.shape[0]
active = patients[patients["current_status"] == "Hospitalized"].shape[0]
recovered = patients[patients["current_status"] == "Recovered"].shape[0]
deaths = patients[patients["current_status"] == "Deceased"].shape[0]

options = [
    {"label": "All", "value" : "All"},
    {"label": "Hospitalized", "value" : "Hospitalized"},
    {"label": "Recovered", "value" : "Recovered"},
    {"label": "Deceased", "value" : "Deceased"}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Corona Virus Pandemic", style={'color': '#fff', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.H3("Total Cases", className='text-light'),
                html.H4(total, className='text-light')
            ], className='card-body')
        ], className='card bg-danger'),
        html.Div([
            html.Div([
                html.H3("Active Cases", className='text-light'),
                html.H4(active, className='text-light')
            ], className='card-body')
        ], className='card bg-info'),
        html.Div([
            html.Div([
                html.H3("Recovered Cases", className='text-light'),
                html.H4(recovered, className='text-light')
            ], className='card-body')
        ], className='card bg-warning'),
        html.Div([
            html.Div([
                html.H3("Death Cases", className='text-light'),
                html.H4(deaths, className='text-light')
            ], className='card-body')
        ], className='card bg-success'),
    ], className='row d-flex justify-content-center', style={'margin-bottom': '20px','margin-top': '20px'}),  # Center the cards using d-flex and justify-content-center
    html.Div([], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = "picker",options = options, value = "All"),
                    dcc.Graph(id = "bar")
                ],className = "card-body")
            ],className = "card")
        ],className= "col-md-12", style={'margin-top': '20px'})  # Add margin to top of graph div
    ], className='row')
], className='container')

@app.callback(Output("bar","figure"),[Input("picker","value")])
def update_graph(type):
    if type == "All":
        p_bar = patients["detected_state"].value_counts().reset_index()
        return {"data":[go.Bar(x=p_bar["detected_state"],y =p_bar["count"] )],
                'layout':go.Layout(title = "State Total Count") }
    else:
        filtered_patients = patients[patients["current_status"] == value]
        p = filtered_patients["detected_state"].value_counts().reset_index()
        return {"data": [go.Bar(x=p["detected_state"], y=p["count"])],
                'layout': go.Layout(title="State Total Count")}
if __name__ == "__main__":
    app.run_server(debug = True)