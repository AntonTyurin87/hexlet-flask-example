#from flask import Flask

#app = Flask(__name__)


from datetime import datetime

def app(environ, start_response):
    time = datetime.now()
    data = bytes(f'The time is {time:%b %d %H:%M:%S}', 'utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]

'''
@app.route('/')
def index():
    return 'Hello, World!'


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users_post():
    return 'POST /users'
'''