from bokeh.plotting import curdoc
from bokeh.themes import Theme

my_theme = Theme(json={
    'attrs': {
        'Axis': {
            'axis_label_text_font_size': '20pt',
            'major_label_text_font_size': '15pt'
        },
        'Title': {
            'text_font_size': '15pt'
        },
        'figure': {
            'height': 400
        },
        'Circle': {
            'size': 10
        }

    }
}
)

curdoc().theme = my_theme