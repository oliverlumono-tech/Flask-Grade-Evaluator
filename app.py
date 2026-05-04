from flask import Flask, redirect, url_for

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the mark is "+str(score)

@app.route('/failure/<int:score>')
def failure(score):
    return "The person has failed and the mark is "+str(score)

@app.route('/results/<int:score>')
def results(score):
    results = ''
    if score < 50:
        endpoint = 'failure'
    else:
        endpoint = 'success'
    return redirect(url_for(endpoint, score=score))


if __name__ == '__main__':
    app.run(debug=True)