import plotly.express as px
import pandas as pd
import json
import plotly.io as pio
pio.renderers.default = "notebook"


crime_data = pd.read_csv('Crime rate.csv')


with open('constituency.json') as json_file:
    geojson = json.load(json_file)


fig = px.choropleth_mapbox(crime_data,
                           geojson=geojson,
                           color='Crime rate per 1000',
                           locations="Parliamentary Constituency",
                           featureidkey="properties.PCON13NM",
                           mapbox_style="carto-positron",
                           zoom=8,
                           center={"lat": 51.5074, "lon": 0.0000},
                           opacity=0.5,
                           color_continuous_scale='Viridis',
                           title="Crime rate in every specific area of London (2008)",)

fig.show()
