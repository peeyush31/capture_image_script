import pprint
import requests


html2canvas = open("html2canvas.min.js")
script = open("script.js")

data = html2canvas.read() + script.read()

url = 'https://app.sitesupport.net/v2/sessions/?api_key=a256ed3d65644de5b0e9431ca902f187'


payload = {
    "url": 'https://wikipedia.org',
    "script_embedded": "https://thimbleprojects.org/peeyush18/581551/script.js"
}

headers = {
    "Content-Type": "application/json"
}


def _process_js():
    resp = requests.post(url, json=payload, headers=headers)
    return resp.json()


pp = pprint.PrettyPrinter(depth=10)

pp.pprint(_process_js())
