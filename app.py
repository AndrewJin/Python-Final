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
    return render_template("index.html") 

@app.route("/1006")
def pythonClass():
    return render_template("1006.html")

@app.route("/columbia")
def columbia():
    return "Columbia!!!"
    #return render_template("columbia.html")


#start the server
if __name__ == "__main__":
    app.run()