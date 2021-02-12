from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to home"


@app.route("/bio")
def bio():
    return "This is Jay Bhanushali"


if __name__ == "__main__":
    app.run(debug = True)
