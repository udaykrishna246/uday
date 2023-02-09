import flask
#help(flask)

from flask import Flask,render_template
app = Flask("Simple Flask App")

@app.route('/')
def sample():
     """simple function"""
     return "Hey Geethanjali This is Codegnan"
names = ['codegnan','gist','python']
@app.route('/balaji',methods=['GET'])
def check():
     return names
@app.route('/gist')
def index():
     return render_template('index.html')


app.run()
