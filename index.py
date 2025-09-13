import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go


app = dash.Dash(__name__)
server = app.server



df_data = pd.read_csv('supermarket_sales.csv')
df_data['Date'] = pd.to_datetime(df_data['Date'])

app.layout = html.Div(
    children=[
        html.H5('Cidades:'),
        dcc.Checklist(df_data['City'].value_counts().index,
        df_data['City'].value_counts().index, id='check_city'),

        html.H5('Variável de análise:'),
        dcc.RadioItems(['Gross income', 'Rating'], 'Gross income', id='main variable'),

        dcc.Graph(id="city_fig"),
        dcc.Graph(id="pay_fig"),
        dcc.Graph(id="income_per_product_fig")

    ]
)







if __name__ =='__main__':
    app.run(debug=True)