import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import pandas as pd

font_awesome1 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css'
font_awesome2 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/regular.min.css'
font_awesome3 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/solid.min.css'
meta_tags = [{'name': 'viewport', 'content': 'width=device-width'}]
external_stylesheets = [font_awesome1, meta_tags]

df = pd.read_csv('jupyternotebook/update.csv')
year_list = list(df['Year'].unique())

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
            """), style={'line-height': '1',
                         'font-size': '17px',
                         'text-align': 'justify',
                         'margin-bottom': '20px'
                         }),

            html.Div(id='calculations')

        ], className='create_container six columns',
            style={'margin-top': '10px',
                   'margin-bottom': '10px'}),

        html.Div([

            html.Div([

                html.P('Year:', className='fix_label', style={
                       'color': 'black', 'margin-top': '15px'}),

                dcc.Slider(id='select_year',
                           min=year_list[0],
                           max=year_list[-1],
                           value=(year_list[0]+year_list[-1])/2,
                           step=1,
                           included=False,
                           updatemode='drag',
                           tooltip={'always_visible': False},
                           marks={str(yrs): str(yrs) for yrs in range(
                               year_list[0], year_list[-1], 2)},
                           className='slider_component')

            ], className='container_slider')

        ], className='create_container six columns',
            style={'margin-top': '10px',
                   'margin-bottom': '10px'})

    ], className='row flex_display')

], className='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})


@app.callback(Output('calculations', 'children'), [Input('select_year', 'value')])
def display_data(select_year):

    df1 = df.groupby(['genre', 'Year'])['total_gross'].sum().reset_index()
    df2 = df1[(df1['genre'] == 'Musical') & (
        df1['Year'] == select_year)]['total_gross'].sum()
    df3 = df1['total_gross'].sum()
    df4 = (df2 / df3) * 100

    df5 = df1[(df1['genre'] == 'Comedy') & (
        df1['Year'] == select_year)]['total_gross'].sum()
    df6 = (df5 / df3) * 100

    df7 = df1[(df1['genre'] == 'Adventure') & (
        df1['Year'] == select_year)]['total_gross'].sum()
    df8 = (df7 / df3) * 100

    df9 = df1[(df1['genre'] == 'Romantic Comedy') & (
        df1['Year'] == select_year)]['total_gross'].sum()
    df10 = (df9 / df3) * 100

    return [
        html.Table([

            html.Thead([

                html.Tr([

                    html.Th('Genre'),
                    html.Th('Symbol'),
                    html.Th('Gross Sales ($)' + ' ' + str(select_year)),
                    html.Th('% Share' + ' ' + str(select_year))

                ], className='header_hover')

            ]),

            html.Tbody([

                html.Tr([

                    html.Td('Musical'),
                    html.Td(html.I(className='fa fa-music',
                            style={'font-size': '150%'})),
                    html.Td('$ {0:,.0f}'.format(df2)),
                    html.Td('{0:,.1f} %'.format(df4))

                ], className="hover_only_row"),

                html.Tr([

                    html.Td('Comedy'),
                    html.Td(html.I(className='fa fa-masks-theater',
                            style={'font-size': '150%'})),
                    html.Td('$ {0:,.0f}'.format(df5)),
                    html.Td('{0:,.1f} %'.format(df6))

                ], className="hover_only_row"),

                html.Tr([

                    html.Td('Adventure'),
                    html.Td(html.I(className='fa-brands fa-space-awesome',
                            style={'font-size': '150%'})),
                    html.Td('$ {0:,.0f}'.format(df7)),
                    html.Td('{0:,.1f} %'.format(df8))

                ], className="hover_only_row"),

                html.Tr([

                    html.Td('Romantic Comedy'),
                    html.Td(html.I(className='fa-solid fa-face-kiss-wink-heart',
                            style={'font-size': '150%'})),
                    html.Td('$ {0:,.0f}'.format(df9)),
                    html.Td('{0:,.1f} %'.format(df10))

                ], className="hover_only_row")

            ])

        ], className='table_style')

    ]


if __name__ == '__main__':
    app.run_server(debug=True)
