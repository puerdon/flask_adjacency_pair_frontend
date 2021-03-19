from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True      
app.jinja_env.auto_reload = True

@app.route('/')
def hello_world():
    return render_template('index.html')
