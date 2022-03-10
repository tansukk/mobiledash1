



from bokeh.models.sources import ColumnDataSource
from flask import Flask, render_template, flash, request, url_for, redirect, send_file
from numpy.lib.utils import source
from bokeh_separate_class_test import myfigure

from bokeh.layouts import layout
from bokeh.models.glyphs import Circle
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, output_file, save
from bokeh.io import curdoc, show
from numpy import source

from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, Band, Toggle, Div
from bokeh.models.annotations import Label, LabelSet, Span, BoxAnnotation, ToolbarPanel
from bokeh.models.widgets import Select, Slider, RadioButtonGroup
from bokeh.layouts import gridplot, row, column
from bokeh.io import curdoc
from bokeh.transform import dodge
from bokeh.resources import CDN
from math import pi

from bokeh.embed import server_document, components



app = Flask(__name__)




@app.route('/')
@app.route('/dash1')
def dash1():

    data_dict = {
    "a": [2,2,3,3,4],
    "b": [5,4,3,2,1]
    }
    #new_figure = myfigure(data_dict, 20)
    #new_figure.draw_figure()

    source=ColumnDataSource(data_dict)
    f = figure(plot_width=140, plot_height=90)
    f.square(x="a", y="b", color="orangered", fill_alpha=.5 , size=8, source=source)
    
    f.toolbar.logo = None
    f.toolbar_location = None
    f.xaxis.visible = True
    f.yaxis.visible = True
    f.xgrid.grid_line_color = None
    f.ygrid.grid_line_color = None
    f.xaxis.minor_tick_line_color = None
    f.xaxis.major_tick_line_color = None
    f.yaxis.minor_tick_line_color = None
    f.yaxis.major_tick_line_color = None
    f.yaxis.major_label_text_font_size = "8px"
    f.xaxis.major_label_text_font_size = "8px"

    f2 = figure(plot_width=140, plot_height=90)
    f2.square(x="a", y="b", color="orangered", fill_alpha=.5 , size=8, source=source)
    
    f2.toolbar.logo = None
    f2.toolbar_location = None
    f2.xaxis.visible = True
    f2.yaxis.visible = True
    f2.xgrid.grid_line_color = None
    f2.ygrid.grid_line_color = None
    f2.xaxis.minor_tick_line_color = None
    f2.xaxis.major_tick_line_color = None
    f2.yaxis.minor_tick_line_color = None
    f2.yaxis.major_tick_line_color = None
    f2.yaxis.major_label_text_font_size = "8px"
    f2.xaxis.major_label_text_font_size = "8px"

    
    graph_layout = gridplot([[f, f2]  ], sizing_mode='fixed', toolbar_location=None)
    #graph_layout.toolbar.logo = None
    #graph_layout.toolbar_location = None
    script, div = components(graph_layout)
    

    return render_template("dash1.html", script=script, div=div)



if __name__ == "__main__":
    app.run(debug=True)
