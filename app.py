from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<p>COba</p>"

if __name__=='__main__':
    app.run(debug=True, port=3000)