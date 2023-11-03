import json

from flask import Flask, render_template
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super().__init__(url_map)
        self.regex = items[0]

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def home():
    return 'Hello, World!'


@app.route("/single/<level>")
def single(level):
    # Opening JSON file
    with open('vizinput/s' + level + '.json') as json_file:
        data = json.load(json_file)
    return render_template('tier.html', data=data, title='S'+level)


@app.route("/double/<level>")
def double(level):
    # Opening JSON file
    with open('vizinput/d' + level + '.json') as json_file:
        data = json.load(json_file)
    return render_template('tier.html', data=data, title='D'+level)


@app.route("/detail/single/<level>")
def detail_single(level):
    # Opening JSON file
    with open('vizinput/s' + level + '.json') as json_file:
        data = json.load(json_file)
    return render_template('detail.html', data=data, title='S'+level)


@app.route("/detail/double/<level>")
def detail_double(level):
    # Opening JSON file
    with open('vizinput/d' + level + '.json') as json_file:
        data = json.load(json_file)
    return render_template('detail.html', data=data, title='D'+level)

