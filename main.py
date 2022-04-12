from flask import Flask, request

app = Flask(_name_)

@app.route('/')
def base_route():
    return "question 3"

@app.route('/<user_name>')
def print_name(user_name):
    return f"welcome {user_name}"

if _name_ == "_main_":
    app.run(host = "0.0.0.0",port = 8080, debug = True)