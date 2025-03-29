#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Print string route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print to console
    return text  # Display on web browser

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    result = ""
    for i in range(parameter):
        result += f'{i}\n'
    return result


# Math operations route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # Division
        if num2 == 0:
            return "Error: Division by zero is undefined", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)



