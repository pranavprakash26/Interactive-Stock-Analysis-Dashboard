import math
import datetime as dt
import numpy as np
import yfinance as yf
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2

def calculate_indicators(df, indicators):
    if "100 Day SMA" in indicators:
        df['100 Day SMA'] = df['Close'].rolling(window=100).mean()
    if "30 Day SMA" in indicators:
        df['30 Day SMA'] = df['Close'].rolling(window=30).mean()
    if "Linear Regression Line" in indicators:
        x = np.arange(len(df))
        coeffs = np.polyfit(x, df['Close'], 1)
        df['Linear Regression Line'] = np.polyval(coeffs, x)
    return df

def plot_data(df, indicators, sync_axis=None):
    df = calculate_indicators(df, indicators)
    gain = df['Close'] > df['Open']
    loss = df['Open'] > df['Close']
    width = 12 * 60 * 60 * 1000

    if sync_axis is not None:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000, x_range=sync_axis)
    else:
        p = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000)

    p.xaxis.major_label_orientation = math.pi / 4
    p.grid.grid_line_alpha = 0.25

    p.segment(df.index, df['High'], df.index, df['Low'])
    p.vbar(df.index[gain], width, df['Open'][gain], df['Close'][gain], fill_color="green", line_color="green")
    p.vbar(df.index[loss], width, df['Open'][loss], df['Close'][loss], fill_color="red", line_color="red")

    if "100 Day SMA" in indicators:
        p.line(df.index, df['100 Day SMA'], color='blue', legend_label='100 Day SMA')
    if "30 Day SMA" in indicators:
        p.line(df.index, df['30 Day SMA'], color='orange', legend_label='30 Day SMA')
    if "Linear Regression Line" in indicators:
        p.line(df.index, df['Linear Regression Line'], color='purple', legend_label='Linear Regression Line')

    return p

def on_button_click():
    ticker1 = stock1_text.value
    ticker2 = stock2_text.value
    start = date_picker_from.value
    end = date_picker_to.value
    indicators = indicator_choice.value

    df1, df2 = load_data(ticker1, ticker2, start, end)
    p1 = plot_data(df1, indicators)
    p2 = plot_data(df2, indicators, sync_axis=p1.x_range)

    curdoc().clear()
    curdoc().add_root(layout)
    curdoc().add_root(row(p1, p2))

stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")

date_picker_from = DatePicker(title="Start Date", value="2024-01-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
date_picker_to = DatePicker(title="End Date", value="2024-02-01", min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))

indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])

load_button = Button(label="Load Data", button_type="success")
load_button.on_click(on_button_click)

layout = column(stock1_text, stock2_text, date_picker_from, date_picker_to, indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)
