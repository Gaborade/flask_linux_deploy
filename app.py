from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>The end is nigh</h1>'




if __name__ == "__main__":
    app.run(port=5000, debug=False)