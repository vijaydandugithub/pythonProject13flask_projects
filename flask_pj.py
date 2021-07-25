#import flask
from flask import Flask,render_template


web_page = Flask(__name__)
web_page.run(debug=True)