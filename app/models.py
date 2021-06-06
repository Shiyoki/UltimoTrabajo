from . import db
from random import randrange

#Modelo de base de datos del producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(10), nullable=False)
    descripcion = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(10), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    bodega = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    precioTotal= db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Producto('{self.codigo}', '{self.descripcion}', '{self.categoria}', '{self.stock}', '{self.bodega}', '{self.precio}', '{self.iva}', '{self.precioTotal}')"

#Modelo de base de datos de la categoria
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codcate = db.Column(db.Integer, nullable=False)
    nomcate = db.Column(db.String(20), nullable=False)
    tipocate = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Categoria('{self.codcate}', '{self.nomcate}', '{self.tipocate}')"

    def generar_codigo(self, numero):
        return randrange(100, 6000)
