from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def populate_db():

def get_quote():

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
