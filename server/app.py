#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"
@app.route('/print/<string:param>')
def print_string(param):
    print(f"{param}")
    return f"{param}"
@app.route('/count/<int:num>')
def count(num):
    output = ""
    for i in range(num):
        output += f"{i}\n"
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, num2, operation):
    if operation=='+':
        result= num1+num2
        return f"{result}"
    elif operation=='-':
        result= num1-num2
        return f"{result}"
    elif operation=='div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result= num1/num2
        return f"{result}"
    elif operation=='*':
        result= num1*num2
        return f"{result}"
    else :
        if num2 == 0:
            return "Modulo by zero is not allowed."
        result= num1%num2
        return f"{result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
