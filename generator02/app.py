from flask import Flask
from os import getenv
from random import randint

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/random")
def random_generator():
    no_of_phaes = 4
    return str(randint(1,no_of_phaes))

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)
