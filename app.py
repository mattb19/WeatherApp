from flask import Flask, request, render_template
from flask_session import Session
import sqlite3
import json
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_modals import Modal
from flask_modals import render_template_modal


app = Flask(__name__)
modal = Modal(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'secret!'
Session(app)


@app.route("/")
def home():
    return render_template("home.html")