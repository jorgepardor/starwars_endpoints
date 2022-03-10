from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    user_password = Column(String(32), nullable=False)
    user_avatar = Column(String(64))
    is_active= Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorite', backref = 'user')

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "user_avatar": self.user_avatar,
        }

class Favorite(db.Model):
    id = Column(Integer, primary_key=True)
    ship_id = Column(Integer, ForeignKey('starships.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    char_id = Column(Integer, ForeignKey('characters.id'))

    def serialize(self):
        return {
            "id": self.id,
            "ship_id": self.ship_id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "char_id": self.char_id,
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False)
    gender_id = Column(Integer, ForeignKey('gender_select.id'))
    image = Column(String(250))
    height = Column(Float)
    mass = Column(Integer)
    hair_color = Column(Integer, ForeignKey('color_select.id'))
    skin_color = Column(Integer, ForeignKey('color_select.id'))
    eye_color = Column(Integer, ForeignKey('color_select.id'))
    birth_year = Column(Integer)
    favorites = db.relationship('Favorite', backref = 'characters')

    def serialize(self):
        return {
            "name": self.name,
            "gender_id": self.gender_id,
            "image": self.image,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)
    image = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate_id = Column(Integer, ForeignKey('climate_select.id'))
    terrain_id = Column(Integer, ForeignKey('terrain_select.id'))
    surface_water = Column(Integer)
    favorites = db.relationship('Favorite', backref = 'planets')

    def serialize(self):
        return {
            "name": self.name,
            "image": self.image,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate_id": self.climate_id,
            "terrain_id": self.terrain_id,
            "surface_water": self.surface_id,
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)
    image = Column(String(250))
    starship_class = Column(Integer, ForeignKey('ship_class_select.id'))
    manufacturer = Column(Integer, ForeignKey('ship_maker_select.id'))
    cost_in_credits = Column(Integer)
    lenght = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmospheric_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    mglt = Column(Integer)
    cargo_capacity = Column(Integer)
    consumable = Column(Integer)
    favorites = db.relationship('Favorite', backref = 'starships')

    def serialize(self):
        return {
            "name": self.name,
            "image": self.image,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "lenght": self.lenght,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmospheric_speed": self.max_atmospheric_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "cargo_capacity": self.cargo_capacity,
            "consumable": self.consumable,
        }

class Homeworld(db.Model):
    __tablename__ = 'homeworld'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

class Pilots(db.Model):
    __tablename__ = 'pilots'
    id = Column(Integer, primary_key=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), nullable=False)
    char_id = Column(Integer, ForeignKey('characters.id'), nullable=False)

class ClimateSelect(db.Model):
    __tablename__ = 'climate_select'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class TerrainSelect(db.Model):
    __tablename__ = 'terrain_select'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class GenderSelect(db.Model):
    __tablename__ = 'gender_select'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class ColorSelect(db.Model):
    __tablename__ = 'color_select'
    id = Column(Integer, primary_key=True)
    color_name = Column(String(72), nullable=False, unique=True)
    color_value = (String(72))

class ShipClassSelect(db.Model):
    __tablename__ = 'ship_class_select'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)

class ShipMakerSelect(db.Model):
    __tablename__ = 'ship_maker_select'
    id = Column(Integer, primary_key=True)
    name = Column(String(72), nullable=False, unique=True)
