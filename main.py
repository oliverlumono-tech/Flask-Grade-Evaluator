from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
    exp={'score':score, 'res':res}
    return render_template('result.html', result=exp)

@app.route('/failure/<int:score>')
def failure(score):
    return f"The person has failed and the mark is {score}"
@app.route('/results/<int:score>')
def results(score):
    
    if score < 50:
        endpoint = 'failure'
    
    else:
        endpoint = 'success'
    return redirect(url_for(endpoint, score=score))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score=0
    if request.method =='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        C=float(request.form['C'])
        data_science=float(request.form['data_science'])
        total_score=(science+math+C+data_science)/4
    res=''
    
    return redirect(url_for('success', score=total_score))
         
if __name__ == '__main__':
    app.run(debug=True)