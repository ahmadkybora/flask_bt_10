from flask import render_template, redirect, url_for, request, abort
from app.Models.User import User

def index():
    users = User.query.all()
    return render_template("users/index.html", users = users)

def store():
    return "ok"

def show(userId):
    return "ok"

def update(userId):
    return "ok"

def delete(userId):
    return "ok"