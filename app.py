from flask import Flask, render_template
import os 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True      
app.jinja_env.auto_reload = True
app.config['JSON_AS_ASCII'] = False
# CORS(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

