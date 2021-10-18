from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<center><h1>Hello, Flask!</h1></center>"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
