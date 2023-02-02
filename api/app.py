from flask import Flask, jsonify, request 
 
app = Flask(__name__)
 
# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")
 
 
if __name__ == "__main__":
    app.run(debug=True)