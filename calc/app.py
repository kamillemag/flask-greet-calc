# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def add_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a,b)
    return str(sum)

@app.route('/sub')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    difference = sub(a,b)
    return str(difference)

@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    product = mult(a,b)
    return str(product)

@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    quotient = div(a,b)
    return str(quotient)

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def any_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operation](a,b)
    return str(result)
