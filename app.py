
from flask import Flask, render_template
from Bio.Seq import Seq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise1')
def exercise1():
    return render_template('exercises/exercise1.html')

@app.route('/exercise2')
def exercise2():
    return render_template('/exercises/exercise2.html')

@app.route('/exercise3')
def exercise3():
    return render_template('/exercises/exercise3.html')

@app.route('/exercise4')
def exercise4():
    return render_template('/exercises/exercise4.html')

@app.route('/exercise5')
def exercise5():
    return render_template('/exercises/exercise5.html')


if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
   