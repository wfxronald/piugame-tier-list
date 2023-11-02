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


@app.route("/double/<level>")
def double(level):
    # Opening JSON file
    with open('vizinput/d' + level + '.json') as json_file:
        data = json.load(json_file)
    return render_template('double.html', data=data, title='D'+level)
