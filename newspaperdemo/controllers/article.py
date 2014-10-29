from flask import Blueprint, render_template, request

mod = Blueprint('article', __name__)

@mod.route('/article')
def index():
    return render_template('article/index.html')