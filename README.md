# flask_reverse_proxy_template
Example project demonstrating flask_reverse_proxy_fix

## Demo verifying url_for in python and in jinja templates
- https://pypi.org/project/flask-reverse-proxy-fix/

Usage

This middleware requires one parameter, a Flask config option, REVERSE_PROXY_PATH_PREFIX, for the path prefix value.

Note: The prefix value SHOULD include a preceding slash, it SHOULD NOT include a trailing slash (i.e. use /foo not /foo/).

A minimal application would look like this:
~~~~
from flask import Flask, url_for
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix

app = Flask(__name__)

app.config['REVERSE_PROXY_PATH'] = '/foo'
ReverseProxyPrefixFix(app)

@app.route('/')
def hello_world():
    return url_for('.hello_world')

~~~~

I have added a jinja template `"{{ url_for('hello_world') }}" ` to verify that it also works inside of a template, which is what I was having trouble with before finding `flask_reverse_proxy_fix'

