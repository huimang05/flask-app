from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=False, port=5001)
=======
    app.run(debug=False)
>>>>>>> bugfix/config

@app.route('/login')
def login():
    return "Login Page"    
