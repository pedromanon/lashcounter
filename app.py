import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import math

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Sets up the left lash input
        left = int(request.form.get("leftlash"))
        if left == None:
            left = 0

        # Sets up the right lash input
        right = int(request.form.get("rightlash"))
        if right == None:
            right = 0

        balance = left - right

        balance_eye = "None"

        if balance < 0:
            balance_eye = "left"
        elif balance > 0:
            balance_eye = "right"

        balance = int(math.fabs(balance))

        both = int(math.ceil((50 - balance) / 2))

        # if 2 * both + left + right + balance > 120:
        #     both = int(math.ceil((120 - (left + right + balance)) / 2))

        extra = 0

        if left + right + balance + (2 * both) < 120:
            extra = int(120 - (left + right + balance + 2 * both))

        extra_individual = int(extra / 2)
        
        return render_template("index.html", left = left, right = right, balance = balance, balance_eye = balance_eye, both = both, extra = extra, extra_individual = extra_individual)
    else:
        return render_template("layout.html")