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
        
    ]
)







if __name__ =='__main__':
    app.run_server(port=8050, debug=True)