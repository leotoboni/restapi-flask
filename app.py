from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
        'db': 'users',
        'host': 'mongodb',
        'port': 27017,
        'username': 'admin',
        'password': 'admin'
}

api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):
        return {"message": "test"}

    def get(self, cpf):
        return {"message": "CPF"}


api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
