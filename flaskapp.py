from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Welcome to Flask Application!"

@app.route("/webhoook")
def pontuado():
    return "Webhooks"    


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    