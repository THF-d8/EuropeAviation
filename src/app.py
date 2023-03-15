import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


# Load the data
df = pd.read_csv("../data/preprocessed_data.csv")

# define app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

server = app.server

app.layout = dbc.Container([
    html.H1("✈ European Flight Dashboard", style={"color": "slateblue", "font-weight": "bold"}),
    html.Div([
        html.Div([
            html.Div([
                html.Label("Please select the year", style={"color": "dimgrey"}),
                html.Div(dcc.Dropdown(
                    id="year",
                    options=[{"label": str(year), "value": year} for year in df['Year'].unique()],
                    value=2016,
                    clearable=False,
                )),
            ], className="mb-3")
        ], className='six columns'),
        html.Div([
            html.Div([
                html.Label("Please select the month", style={"color": "dimgrey"}),
                html.Div(dcc.Dropdown(
                    id="month",
                    options=[{"label": str(month), "value": month} for month in df['Month'].unique()],
                    value=1,
                    clearable=False,
                )),
            ], className="mb-3")
        ], className='six columns'),
    ], className='row'),
    html.Div([
        html.Div([
            html.Label("Please specify the flight type", style={"color": "dimgrey"}),
            html.Div(dcc.Dropdown(
                id="flight_type",
                options=[{"label": "Departure", "value": "Departure"},
                         {"label": "Arrival", "value": "Arrival"},
                         {"label": "Total", "value": "Total"}],
                value="Departure",
                clearable=False,
            )),
        ], className="mb-3")
    ], className='row'),
    html.Div([
        dcc.Graph(id="top_airport_bar_chart"),
        dcc.Graph(id="top_airport_line_chart")
    ])
], fluid=True, className="bg-light p-5")



@app.callback(
    [Output("top_airport_bar_chart", "figure"),
     Output("top_airport_line_chart", "figure")],
    [Input("year", "value"),
     Input("month", "value"),
     Input("flight_type", "value")]
)
def update_charts(year, month, flight_type):
    filtered_df = df[(df['Year'] == year) & (df['Month'] == month)]
    top_airport = filtered_df.groupby(['ICAO', 'Airport']).sum().reset_index().sort_values(by=[flight_type], ascending=False)['Airport'].iloc[0]
    top_airport_data = filtered_df[filtered_df['Airport'] == top_airport]

    # Create bar chart
    top_airports = filtered_df.groupby(['ICAO', 'Airport']).sum().reset_index().sort_values(by=[flight_type], ascending=False).head(10)
    bar_chart = px.bar(top_airports, x='ICAO', y=flight_type, text='Airport', color="Airport")
    bar_chart.update_layout(title=f"Top 10 Airports by {flight_type} in {year}-{month}", xaxis_title='Airport ICAO Code', yaxis_title=f'Number of {flight_type} Flights')

    # Create line chart
    line_chart = px.line(top_airport_data, x='Date', y=['Departure', 'Arrival', 'Total'], title=f"Trend of Number of Flights for {top_airport} in {year}-{month}")
    line_chart.update_layout(xaxis_title='Date', yaxis_title='Number of Flights')

    return bar_chart, line_chart

# run app
if __name__ == '__main__':
    app.run_server(debug=True)

