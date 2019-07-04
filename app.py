from flask import Flask, url_for, render_template
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix

app = Flask(__name__)

app.config['REVERSE_PROXY_PATH'] = '/foo'
ReverseProxyPrefixFix(app)

@app.route('/')
def hello_world():
    return url_for('.hello_world')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)