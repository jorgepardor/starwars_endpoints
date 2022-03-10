import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorite

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/seriali
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/character', methods=['GET'])
def list_characters():
    return jsonify(Characters.query.all()), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_serialized= list(map(lambda user:user.serialize(), users))
    return jsonify({'response':users_serialized})

@app.route('/characters', methods=['GET'])
def get_all_characters():
    characters = Characters.query.all()
    characters_serialized= list(map(lambda characters:characters.serialize(), characters))
    return jsonify({'response':characters_serialized})

@app.route('/characters/<int:characters_id>', methods=['GET'])
def get_single_characters(characters_id):
    characters = Characters.query.get(characters_id)
    if characters:
        return jsonify({'response': characters.serialize()}), 200
    else: 
        return jsonify ({'error': 'the user doesnt exist'}), 404
    return jsonify({'response':characters.serialize()})

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_serialized= list(map(lambda planets:planets.serialize(), planets))
    return jsonify({'response':planets_serialized})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
