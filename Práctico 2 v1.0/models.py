from __main__ import app

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    clave = db.Column(db.String(120), nullable=False)
    #relacion con el Usuario y la Receta
    receta = db.relationship('Receta', backref='usuario', cascade='all, delete-orphan')
class Receta(db.Model):
    __tablename__ = 'receta'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True)
    tiempo = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    elaboracion = db.Column(db.Text)
    cantidadmegusta = db.Column(db.Integer)
    usuarioid = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    #relación con la Receta y el Ingrediente
    ingrediente = db.relationship('Ingrediente', backref='receta', cascade='all, delete-orphan')
class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True)
    cantidad = db.Column(db.Float)
    unidad = db.Column(db.String(20))
    recetaid = db.Column(db.Integer, db.ForeignKey('receta.id'))