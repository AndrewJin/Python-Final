"""
Creates website using Flask.

@author: Andrew Jin
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("main.html") 

@app.route("/assignments")
def pythonClass():
    return render_template("assignments.html")

@app.route("/classes")
def columbia():
    return render_template("classes.html")


#start the server
if __name__ == "__main__":
    app.run()