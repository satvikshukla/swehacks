from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure

output_file("graph.html")

emotions = ['Joy','Sadness', 'Tentative', 'Analytical']
repos = ['average', 'you']

data = {'Emotions' : emotions,
        'average' : [0.58125,0.532308, 0.717059,0.696667,0.532308],
        'you'   : [0.3, 0.4, 0.5, 0.2]
        }


x = [ (emotion, repo) for emotion in emotions for repo in repos ]
counts = sum(zip(data['average'], data['you']), ())

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250, title="Seniment Averages",
           toolbar_location=None, tools="")

p.vbar(x='x', top='counts', width=0.9, source=source)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
