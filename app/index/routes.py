from flask import render_template, url_for, redirect, request, Blueprint
from .. import db
from ..models import *
from .forms import *

index = Blueprint("index", __name__)

#Pagina de inicio
@index.route("/")
@index.route("/home")
def home():
    form = registrarForm()
    return render_template('menu.html', form=form, title="Registrar producto")

#Metodo para ingresar producto
@index.route("/insert", methods=["GET", "POST"])
def insert():
    form = registrarForm()
    if form.validate_on_submit():
        producto = Producto(codigo=form.codigo.data,
                            descripcion=form.descripcion.data,
                            categoria=form.categoria.data,
                            stock=form.stock.data,
                            bodega=form.bodega.data,
                            precio=form.precio.data,
                            iva=((form.iva.data/100)+1),
                            precioTotal=((form.precio.data) + ((form.iva.data/100)+1))) #Formula para mostrar el precio total
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('index.home'))
    return render_template('insert.html', form=form)

#Metodo para ingresar categoria
@index.route("/insertcat", methods=["GET", "POST"])
def insertcat():
    form = registrarcatForm()
    if form.validate_on_submit():
        categoria = Categoria(cod_cate=form.cod_cate.data,
                              nom_cate=form.nom_cate.data,
                              tipo_cate=tipo_cat(form.cod_cate.data))
        db.session.add(categoria)
        db.session.commit()
        return redirect(url_for('index.home'))
    return render_template('insertcat.html', form=form)

#Metodo para mostrar productos
@index.route("/tablaprod")
def tablaprod():
    productos = db.session.query(Producto).all()
    return render_template('tablaprod.html', productos=productos)

#Metodo para mostrar categorias
@index.route("/tablacat")
def tablacat():
    categorias = db.session.query(Categoria).all()
    return render_template('tablacat.html', categorias=categorias)

#Validacion del tipo de categoria
def tipo_cat(numero):
    if numero in range(100, 1500):
        return 'PERSONAL'
    elif numero in range(1501, 3000):
        return 'ANIMAL'
    elif numero in range(3001, 6000):
        return 'HOGAR-FERRETERIA'
