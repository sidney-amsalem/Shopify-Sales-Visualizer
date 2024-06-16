# data_processor.py

import pandas as pd
import plotly.express as px

file_path = 'data/raw/orders_export_1.csv'
data = pd.read_csv(file_path)
df = pd.DataFrame(data)


def create_heatmap(filter=0):
    # Group the data by 'State' and calculate the number of orders and total revenue per state
    summary_df = df.groupby('Shipping Province').agg({'Total': 'sum', 'Name': 'count'}).reset_index()
    summary_df.columns = ['Shipping_Province', 'Total_Revenue', 'Number_of_Orders']

    # Create a colorscale gradient from clear to green
    colorscale = [(0, 'rgba(0,0,0,0)'), (1, 'rgba(0,255,0,1)')]

    data = 'Total_Revenue'
    if filter == 1:
        data = 'Number_of_Orders'


    # Create heatmap using summary_df
    heatmap = px.choropleth(
        summary_df,
        locations='Shipping_Province',
        locationmode="USA-states",
        color=data,
        color_continuous_scale=colorscale,
        scope="usa")

    heatmap.show()
