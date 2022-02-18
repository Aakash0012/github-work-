from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    h=[]
    table = (request.args.get('table'))
    print(table)
    if table==None:
        table=5
    else:
        table=int(table)

    for i in range(1, 11):
        h.append(i*table)
    return render_template('index.html', h=h)

@app.route('/table', methods=['POST', 'GET'])
def table():
    import requests 
    h=[]
    table = int(request.form['table'])

    for i in range(1, 11):
        h.append(i*table)
    return render_template('index.html', h=h)

@app.route('/greet')
def greet():
    return render_template('greet.html')

@app.errorhandler(404)
def page_not_found(e):
    return ( render_template('404.html'), 404 )

if __name__ == '__main__':
    app.run(debug=True)