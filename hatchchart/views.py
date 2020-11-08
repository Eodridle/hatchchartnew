from django.http import HttpResponse
from django.shortcuts import render
import operator
import re
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd


df = pd.DataFrame([
    dict(Bug="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Bug="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Bug="Job C", Start='2009-02-20', Finish='2009-05-30')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Bug")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
#fig.show()

import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

def home(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "home.html", context={'plot_div': app.layout})