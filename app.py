from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = "mahakg290399"
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate,identity) #/auth

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(StoreList, '/stores')
api.add_resource(Store, "/store/<string:name>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)