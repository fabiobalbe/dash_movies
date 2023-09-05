import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd

font_awesome1 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
# font_awesome2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/regular.min.css'
# font_awesome3 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'
meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}]
external_stylesheets = [font_awesome1, meta_tags]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        html.Div([
            html.H5('Movie Data Analyzer', className='title_text')
        ], className='title_container twelve columns')
    ], className='row flex_display'),
    
    html.Div([

        html.Div([

            html.P(dcc.Markdown("""
                **Below table** shows gross sales **values** for each genre
                category and **percentage** of share for each genre category
                in **each year**.
            """), style={'line-height':'1',
                         'font-size':'17px',
                         'text-align':'justify',
                         'margin-bottom':'20px',
                         })

        ], className='create_container six columns',
                 style={'margin-top':'10px',
                        'margin-bottom':'10px'})

    ], className='row flex_display')

], className='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})

if __name__ == '__main__':
    app.run_server(debug=True)
