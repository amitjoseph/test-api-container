from flask import Flask,make_response
import sys,os

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Hello!'

@app.route('/health')
def health():
    return 'Application is working!'

@app.route('/echo/<string>')
def echo(string):
    return string

@app.route('/env/all')
def env_all():
    return str(os.environ)

@app.route('/env/<string>')
def env(string):
    return os.environ.get(string)

@app.route('/file/<path:string>')
def file(string):
    filename = "../" + string
    f = open(filename, "r")
    response = make_response(f.read(), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/return',defaults={'status_code': 200, 'string':'Hello!'})
@app.route('/return//<status_code>',defaults={'string':'Hello!'})
@app.route('/return/<status_code>/<string>')
def creturn(status_code,string):
    return string,status_code

@app.route('/kill')
def kill():
    sys.exit(4)