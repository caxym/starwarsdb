from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    favorito = db.relationship('Favorito')

    def user_list(self):
        return{
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email
        }


class Favorito(db.Model):
    __tablename__ = 'favorito'
    id = db.Column(db.Integer, primary_key=True)
    name_personajes = db.Column(db.String(50),ForeignKey('personaje.name'))
    name_vehiculos = db.Column(db.String(50),ForeignKey('vehiculo.name'))
    name_planetas = db.Column(db.String(50),ForeignKey('planeta.name'))
    user_email = db.Column(db.String(50),ForeignKey('user.email'))

    def user_favorite(self):
        return{
            'id': self.id,
            'name_personajes': self.name_personajes,
            'name_vehiculos': self.name_vehiculos,
            'name_planetas': self.name_planetas
        }

class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50),nullable=False)
    species = db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(50),nullable=False)
    homeworld = db.Column(db.String(50),nullable=False)
    height = db.Column(db.String(50),nullable=False)
    mass = db.Column(db.String(50),nullable=False)
    bornLocation = db.Column(db.String(50),nullable=False)
    deadLocation = db.Column(db.String(50),nullable=False)
    favorito = db.relationship('Favorito')

    def user_personaje(self):
        return{
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'gender': self.gender,
            'homeworld': self.homeworld,
            'height': self.height,
            'mass': self.mass,
            'bornLocation': self.bornLocation,
            'deadLocation': self.deadLocation
        }

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50),nullable=False)
    model = db.Column(db.String(50),nullable=False)
    passengers = db.Column(db.String(50),nullable=False)
    cargo_capacity = db.Column(db.String(50),nullable=False)
    crew = db.Column(db.String(50),nullable=False)
    length = db.Column(db.String(50),nullable=False)
    starship_class = db.Column(db.String(50),nullable=False)
    cost_in_credits = db.Column(db.String(50),nullable=False)
    favorito = db.relationship('Favorito')

    def user_vehiculo(self):
        return{
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'crew': self.crew,
            'length': self.length,
            'starship_class': self.starship_class,
            'cost_in_credits': self.cost_in_credits
        }

class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50),nullable=False)
    climate = db.Column(db.String(50),nullable=False)
    terrain = db.Column(db.String(50),nullable=False)
    population = db.Column(db.String(50),nullable=False)
    diameter = db.Column(db.String(50),nullable=False)
    gravity = db.Column(db.String(50),nullable=False)
    rotation_period = db.Column(db.String(50),nullable=False)
    surface_water = db.Column(db.String(50),nullable=False)
    favorito = db.relationship('Favorito')

    def user_planeta(self):
        return{
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
            'diameter': self.diameter,
            'gravity': self.gravity,
            'rotation_period': self.rotation_period,
            'surface_water': self.surface_water
        }