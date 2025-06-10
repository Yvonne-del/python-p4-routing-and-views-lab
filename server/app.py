#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = "\n".join(str(i) for i in range(parameter)) + "\n"
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        n = num1 + num2
        return str(n)
    elif operation == '-':
        n = num1 - num2
        return str(n)
    elif operation == '*':
        n = num1 * num2
        return str(n)
    elif operation == 'div':
        n = num1 / num2
        return str(n)
    elif operation == '%':
        n = num1 % num2
        return str(n)
    else:
        return 'Invalid characters'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
