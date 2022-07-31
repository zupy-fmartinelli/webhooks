from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Welcome to Flask Application!"

@app.route('/webhooks')
def zupyhooks():
    return 'Hello, World'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    