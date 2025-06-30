from flask_migrate import Migrate
from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello World"


@app.route("/home")
def home():
    return "hello home"


# import user_controller
# import controller.user_controller as user_controller
# import controller.product_controller as product_controller
# from controller import user_controller, product_controller

from controller import *  # This will not work we have to tell the python that controller is not just a folder its a python package for that we have to introduced __init__.py file in controller
