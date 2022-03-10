import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorite, Starships

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

# Generating endpoints for all the listed users and to display all the available info on a single user

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_serialized= list(map(lambda user:user.serialize(), users))
    return jsonify({'response':users_serialized})

@app.route('/user/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'response': user.serialize()}), 200
    else: 
        return jsonify ({'error': 'the user doesnt exist'}), 404
    return jsonify({'response':user.serialize()})

# Generating endpoints for all the listed characters and to display all the available info on a single character

@app.route('/characters', methods=['GET'])
def get_all_characters():
    characters = Characters.query.all()
    characters_serialized= list(map(lambda characters:characters.serialize(), characters))
    return jsonify({'response':characters_serialized})

@app.route('/character/<int:characters_id>', methods=['GET'])
def get_single_characters(characters_id):
    characters = Characters.query.get(characters_id)
    if characters:
        return jsonify({'response': characters.serialize()}), 200
    else: 
        return jsonify ({'error': 'the user doesnt exist'}), 404
    return jsonify({'response':characters.serialize()})

# Generating endpoints for all the listed planets and to display all the available info on a single planet

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_serialized= list(map(lambda planets:planets.serialize(), planets))
    return jsonify({'response':planets_serialized})

@app.route('/planet/<int:planets_id>', methods=['GET'])
def get_single_planets(planets_id):
    planets = Planets.query.get(planets_id)
    if planets:
        return jsonify({'response': planets.serialize()}), 200
    else: 
        return jsonify ({'error': 'the planet doesnt exist'}), 404
    return jsonify({'response':planets.serialize()})

# Generating endpoints for all the listed ships and to display all the available info on a single ship

@app.route('/starships', methods=['GET'])
def get_all_starships():
    starships = Starships.query.all()
    starships_serialized= list(map(lambda starships:starships.serialize(), starships))
    return jsonify({'response':starships_serialized})

@app.route('/starship/<int:starships_id>', methods=['GET'])
def get_single_starships(starships_id):
    starships = Starships.query.get(starships_id)
    if starships:
        return jsonify({'response': starships.serialize()}), 200
    else: 
        return jsonify ({'error': 'the starship doesnt exist'}), 404
    return jsonify({'response':starships.serialize()})

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
