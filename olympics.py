from bokeh.charts import Bar, show, output_file, Donut
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
from bokeh.layouts import row
from bokeh.models import HoverTool
import pandas as pd

# get the data and store in data frame
df = df_from_json(data)
# filter out those countries which have less than 8 medals
df = df[df['total'] > 8]
# sort the data
df = df.sort_values(by="total", ascending=False)

# melt the data for first bar chart
df1 = pd.melt(df, id_vars=['abbr'],
             value_vars=['bronze', 'silver', 'gold', 'total'],
             value_name='medal_count', var_name='medal')

bar1 = Bar(df1, values='medal_count', label='abbr', agg='mean'
			, group=['medal'], title="Olympics Mdeals"
			, color=['brown', 'silver', 'gold', 'green']
			, plot_width=1000, tools='hover')

# set the tooltip for detail information of the bars
hover1 = bar1.select(dict(type=HoverTool))
hover1.tooltips = [('medals', '@height'), ('Country', '@abbr')]

output_file("bar1.html")

# melt the data for second bar chart
df2 = pd.melt(df, id_vars=['abbr'],
             value_vars=['bronze', 'silver', 'gold'],
             value_name='medal_count', var_name='medal')

bar2 = Bar(df2, values='medal_count', label='abbr', agg='mean'
			, stack=['medal'], title="Olympics Mdeals"
			, color=['brown', 'silver', 'gold']
			, plot_width=1000, tools='hover')

# set the tooltip for detail information of the bars
hover2 = bar2.select(dict(type=HoverTool))
hover2.tooltips = [('medals', '@height'), ('Country', '@abbr')]

output_file("bar2.html")