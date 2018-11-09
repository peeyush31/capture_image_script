import json
from upload_file import get_presigned_url
from quart import Quart, request, url_for,make_response
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('templates', 'base'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Quart(__name__)


@app.route('/presigned-url')
async def progress():
    file_name = request.args.get("file", "test.png")
    if "file" not in request.args and "SURFLY" in request.args:
        file_name = request.args["SURFLY"].split("file=")[1]
    response = await make_response(
        json.dumps({"url": get_presigned_url(file_name)}),
        {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
            'Transfer-Encoding': 'chunked',
            'Access-Control-Allow-Origin': '*'
        },
    )
    return response

@app.route('/capture-script')
async def capture_script():
    return open("script.js")

@app.route('/')
async def index():
    return env.get_template('base.html').render(url=url_for('progress'))


if __name__ == "__main__":
    app.run('localhost', port=5001, debug=True)


