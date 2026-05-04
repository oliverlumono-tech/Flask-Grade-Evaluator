from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    # Make sure 'index.html' exists in a folder named 'templates'
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return f"The person has passed and the mark is {score}"

@app.route('/failure/<int:score>')
def failure(score):
    return f"The person has failed and the mark is {score}"

@app.route('/results/<int:score>')
def results(score):
    # Removed the unused 'results' variable
    if score < 50:
        endpoint = 'failure'
    else:
        endpoint = 'success'
    return redirect(url_for(endpoint, score=score))
###result checker html page
#@app.route('/submit', methods=['POST', 'GET'])
#def submit():


if __name__ == '__main__':
    app.run(debug=True)