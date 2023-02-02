# THIS REPOSITORY IS NO LONGER MAINTAINED AND HAS BEEN ARCHIVED

## flask_reverse_proxy_template
Example project demonstrating flask_reverse_proxy_fix

## Simple demo flask application verifying url_for in python and in jinja templates work with 


Example usage from: https://pypi.org/project/flask-reverse-proxy-fix/
    
> Usage
>
> This middleware requires one parameter, a Flask config option, REVERSE_PROXY_PATH_PREFIX, for the path prefix value.
>
> Note: The prefix value SHOULD include a preceding slash, it SHOULD NOT include a trailing slash (i.e. use /foo not /foo/).
>
> A minimal application would look like this:
    
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

I added a jinja template `"{{ url_for('hello_world') }}" ` to verify that it also works inside of a template.

app.py
~~~~
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
~~~~

hello.html
~~~~
<a href="{{ url_for('hello_world') }}">Hello world Link</a>
~~~~

`url_for()` resolving correctly, when reverse proxied, inside a template is what I was having trouble with before finding `flask_reverse_proxy_fix`

----------------

Thank you to  British Antarctic Survey for the `flask_reverse_proxy_fix` package.
Their license can be found here: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

