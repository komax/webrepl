#!/usr/bin/env python
from flask import Flask, render_template

webrepl_app = Flask(__name__)

@webrepl_app.route('/webrepl')
def index():
    return render_template('webrepl.html')

if __name__ == '__main__':
    webrepl_app.run(debug=True)