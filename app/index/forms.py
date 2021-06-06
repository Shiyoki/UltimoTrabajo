from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, validators, ValidationError, SubmitField
from wtforms.validators import DataRequired, Length
from ..models import *
from re import match, findall

#Formulario del producto
class registrarForm(FlaskForm):
    codigo = StringField('Codigo del producto', validators=[DataRequired("Este campo es obligatorio"),
                                                            Length(min=5, max=5, message="El codigo debe contener 5 caracteres")])
    descripcion = StringField('Nombre del producto', validators=[DataRequired("Este campo es obligatorio")])
    categoria = StringField('Nombre de la categoria', validators=[DataRequired("Este campo es obligatorio")])
    stock = IntegerField('Cantidad del producto en stock', validators=[DataRequired("Este campo es obligatorio")])
    bodega = IntegerField('Numero de bodega', validators=[DataRequired("Este campo es obligatorio")])
    precio = FloatField('Precio del producto', validators=[DataRequired("Este campo es obligatorio")])
    iva = FloatField('Iva del producto', validators=[DataRequired("Este campo es obligatorio")])
    submit = SubmitField('Registrar')

    #Validacion del iva
    def vaidate_iva(self, iva):
        if iva.data <= 0:
            raise ValidationError("Valor de iva incorrecto")

    #Validacion del codigo un caracter y cuatro numeros consecutivos
    def validate_letter(self, codigo):
        if not match(r'\D?', codigo.data):
            raise ValidationError('El codigo debe empezar con una letra')
        elif len(findall(r'\D', codigo.data)) > 1:
            raise ValidationError('Los numeros no son consecutivos')

#Formulario de la categoria
class registrarcatForm(FlaskForm):
    cod_cate = IntegerField('Codigo de la categoria (entre 100 a 6000)', validators=[DataRequired("Este campo es obligatorio"),
                                                        Length(min=100, max=6000, message="El codigo debe estar en un rango entre 100 a 600")])
    nom_cate = StringField('Nombre de la categoria', validators=[DataRequired("Este campo es obligatorio")])
    tipo_cate = StringField('Tipo de categoria', validators=[DataRequired("Este campo es obligatorio")])
    submit = SubmitField('Registrar')