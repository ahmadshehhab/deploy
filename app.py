from flask import Flask
web_app = Flask(__name__)
@web_app.route("/")
def  homepage():    
    
        return "hello"

if __name__ =="main":
    web_app.run()