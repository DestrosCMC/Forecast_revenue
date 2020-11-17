import plotly.graph_objects as go
import numpy as np
import pandas as pd

fig = go.Figure()

x_list = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
atvi = [4447, 4755, 4856, 4583, 4408, 4664, 6608, 7017, 7500, 6489, 7660]
ea = [3654, 3589, 4143, 3797, 3575, 4515, 4396, 4845, 5150, 4950, 5537]
ttwo = [862.2,1136.9,825.8,1214.5,2350.6,1082.9,1413.7,1779.7,1792.9,2668.4,3089.0]

fig.add_trace(go.Scatter(x=x_list, y = ea, fill = 'tonexty', name= 'EA', marker_color= 'red'))
fig.add_trace(go.Scatter(x = x_list, y = atvi, fill = 'tonexty', name = 'Activision', marker_color = 'black'))
fig.add_trace(go.Scatter(x=x_list, y = ttwo, fill = 'tozeroy', name= 'Take-Two', marker_color= 'RoyalBlue'))

fig.update_yaxes(range = [800,8000])
fig.update_xaxes(title_text = 'Year')
fig.update_yaxes(title_text = 'Revenue in Millions')
fig.update_layout(yaxis_tickformat = '$')
fig.update_layout(title_text = 'Revenue Comparison of Competitors')
fig.show()

#fig.write_html()
