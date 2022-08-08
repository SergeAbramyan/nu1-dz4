import requests
import json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    if_by = True
    text = '<h1>Курс обмена валют в MyBank)))</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            if type(v) == float :
                if if_by:
                    text += f'<td>{(v*0.95):.4}</td>'
                    if_by = False
                else:
                    text += f'<td>/{(v * 1.05):.4}</td>'
                    if_by = True
            else:
                text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()