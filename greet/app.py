from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Index Page</h1>"

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"


if __name__ == '__main__':
	app.run(debug=True)