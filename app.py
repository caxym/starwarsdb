from flask import Flask, request, jsonify
from models import db, User, Favorito, Personaje, Vehiculo, Planeta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///starwars.db'
db.init_app(app)

@app.route('/')
def home():
    return "Base de Datos StarWars"

@app.route('/users', methods=['POST'])
def create_user():
    user = User()
    user.name = request.json.get('name')
    user.lastname = request.json.get('lastname')
    user.username = request.json.get('username')
    user.email = request.json.get('email')
    user.password = request.json.get('password')

    db.session.add(user)
    db.session.commit()

    return "usuario guardado"

@app.route('/pj', methods=['POST'])
def create_pj():
    personaje = Personaje()
    personaje.image = request.json.get('image')
    personaje.name = request.json.get('name')
    personaje.species = request.json.get('species')
    personaje.gender = request.json.get('gender')
    personaje.homeworld = request.json.get('homeworld')
    personaje.height = request.json.get('height')
    personaje.mass = request.json.get('mass')
    personaje.bornLocation = request.json.get('bornLocation')
    personaje.deadLocation = request.json.get('deadLocation')

    db.session.add(personaje)
    db.session.commit()

    return "personaje guardado"

@app.route('/ship', methods=['POST'])
def create_ship():
    vehiculo = Vehiculo()
    vehiculo.image = request.json.get('image')
    vehiculo.name = request.json.get('name')
    vehiculo.model = request.json.get('model')
    vehiculo.passengers = request.json.get('passengers')
    vehiculo.cargo_capacity = request.json.get('cargo_capacity')
    vehiculo.crew = request.json.get('crew')
    vehiculo.length = request.json.get('length')
    vehiculo.starship_class = request.json.get('starship_class')
    vehiculo.cost_in_credits = request.json.get('cost_in_credits')

    db.session.add(vehiculo)
    db.session.commit()

    return "Vehiculo guardado"


@app.route('/planet', methods=['POST'])
def create_planet():
    planeta = Planeta()
    planeta.image = request.json.get('image')
    planeta.name = request.json.get('name')
    planeta.climate = request.json.get('climate')
    planeta.terrain = request.json.get('terrain')
    planeta.population = request.json.get('population')
    planeta.diameter = request.json.get('diameter')
    planeta.gravity = request.json.get('gravity')
    planeta.rotation_period = request.json.get('rotation_period')
    planeta.surface_water = request.json.get('surface_water')

    db.session.add(planeta)
    db.session.commit()

    return "Planeta guardado"

@app.route('/favorito', methods=['POST'])
def create_favorito():
    favorito = Favorito()
    favorito.name_personajes = request.json.get('name_personajes')
    favorito.name_vehiculos = request.json.get('name_vehiculos')
    favorito.name_planetas = request.json.get('name_planetas')
    favorito.user_email = request.json.get('user_email')
    

    db.session.add(favorito)
    db.session.commit()

    return "Favorito guardado"

@app.route('/favorito/pj', methods=['POST'])
def create_favorito_pj():
    favorito = Favorito()
    favorito.name_personajes = request.json.get('name_personajes')
    favorito.name_vehiculos = request.json.get('name_vehiculos')
    favorito.name_planetas = request.json.get('name_planetas')
    favorito.user_email = request.json.get('user_email')
    

    db.session.add(favorito)
    db.session.commit()

    return "Favorito guardado"

@app.route('/users/list', methods=['GET'])
def get_list_user():
    users = User.query.all()
    result = []

    for user in users:
        result.append(user.user_list())
    return jsonify(result)

@app.route("/users/<int:id>", methods=["GET"])
def get_oneuser(id):
    user = User.query.get(id)
    if user is not None:
       return jsonify(user.user_list())

@app.route('/pj/list', methods=['GET'])
def get_list_pj():
    personajes = Personaje.query.all()
    result = []

    for personaje in personajes:
        result.append(personaje.user_personaje())
    return jsonify(result)

@app.route("/pj/<int:id>", methods=["GET"])
def get_onepj(id):
    pj = Personaje.query.get(id)
    if pj is not None:
       return jsonify(pj.user_personaje())

@app.route('/ship/list', methods=['GET'])
def get_list_ship():
    vehiculos = Vehiculo.query.all()
    result = []

    for vehiculo in vehiculos:
        result.append(vehiculo.user_vehiculo())
    return jsonify(result)

@app.route("/ship/<int:id>", methods=["GET"])
def get_oneship(id):
    vehiculo = Vehiculo.query.get(id)
    if vehiculo is not None:
       return jsonify(vehiculo.user_vehiculo())

@app.route('/planet/list', methods=['GET'])
def get_list_planet():
    planets = Planeta.query.all()
    result = []

    for planet in planets:
        result.append(planet.user_planeta())
    return jsonify(result)

@app.route("/planet/<int:id>", methods=["GET"])
def get_oneplanet(id):
    planeta = Planeta.query.get(id)
    if planeta is not None:
       return jsonify(planeta.user_planeta())

@app.route('/favorito/list', methods=['GET'])
def get_list_favorito():
    favoritos = Favorito.query.all()
    result = []

    for favorito in favoritos:
        result.append(favorito.user_favorite())
    return jsonify(result)

@app.route('/users/<int:id>', methods=['PUT','DELETE'])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method =='DELETE':
            db.session.delete(user)
            db.session.commit()

            return jsonify(),204
        else:
            user.username = request.json.get('username')

            db.session.commit()

            return jsonify(),200
    
    return jsonify(),404

@app.route('/pj/<int:id>', methods=['PUT','DELETE'])
def update_personaje(id):
    personaje = Personaje.query.get(id)
    if personaje is not None:
        if request.method =='DELETE':
            db.session.delete(personaje)
            db.session.commit()

            return jsonify(),204
        else:
            personaje.name = request.json.get('name')

            db.session.commit()

            return jsonify(),200
    
    return jsonify(),404

@app.route('/ship/<int:id>', methods=['PUT','DELETE'])
def update_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)
    if vehiculo is not None:
        if request.method =='DELETE':
            db.session.delete(vehiculo)
            db.session.commit()

            return jsonify(),204
        else:
            vehiculo.name = request.json.get('name')

            db.session.commit()

            return jsonify(),200
    
    return jsonify(),404

@app.route('/planet/<int:id>', methods=['PUT','DELETE'])
def update_planeta(id):
    planeta = Planeta.query.get(id)
    if planeta is not None:
        if request.method =='DELETE':
            db.session.delete(planeta)
            db.session.commit()

            return jsonify(),204
        else:
            planeta.name = request.json.get('name')

            db.session.commit()

            return jsonify(),200
    
    return jsonify(),404

@app.route('/favorito/<int:id>', methods=['PUT','DELETE'])
def update_favorito(id):
    favorito = Favorito.query.get(id)
    if favorito is not None:
        if request.method =='DELETE':
            db.session.delete(favorito)
            db.session.commit()

            return jsonify(),204
        else:
            favorito.name_personaje = request.json.get('name_personaje')

            db.session.commit()

            return jsonify(),200
    
    return jsonify(),404

with app.app_context():
    db.create_all()

app.run(host='localhost', port='5000')