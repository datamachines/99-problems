from flask import Flask
app = Flask(__name__)

@app.route("/<subject>")
def hello(subject):
    return "Hello " + subject + "!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
