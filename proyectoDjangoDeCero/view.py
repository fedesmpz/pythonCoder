import email
from django.http import HttpResponse
from django.template import loader
from MiFamilia.models import Familiar



def verMisFamiliares(self):
    plantilla = loader.get_template('familia.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def agregarFamilia(self):
    familiar1 = Familiar(tipo="Madre", nombre="Alejandra", apellido="Benito", edad=59, fechaDeNacimiento="1963-03-04", email="albeni@mecon.gov.ar")
    familiar2 = Familiar(tipo="Padre", nombre="Gustavo", apellido="Pezzutti", edad=60, fechaDeNacimiento="1961-08-25", email="gpezzutti@gmail.com")
    familiar3 = Familiar(tipo="Hermano", nombre="Pablo", apellido="Pezzutti", edad=35, fechaDeNacimiento="1987-02-04", email="pablopesu@gmail.com")
    familiar4 = Familiar(tipo="Hermana", nombre="Lucia", apellido="Pezzutti", edad=25, fechaDeNacimiento="1996-10-29", email="lupezzutti@gmail.com")
    familiar5 = Familiar(tipo="Pareja", nombre="William", apellido="Oropeza", edad=30, fechaDeNacimiento="1992-05-19", email="william.oropeza20@gmail.com")
    
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiar5.save()
    
    documento = f'Tipo: {familiar1.tipo} - Nombre: {familiar1.nombre} - Apellido {familiar1.apellido} - Edad: {familiar1.edad} - Fecha de nacimiento: {familiar1.fechaDeNacimiento} - E-Mail: {familiar1.email}<br>Tipo: {familiar2.tipo} - Nombre: {familiar2.nombre} - Apellido {familiar2.apellido} - Edad: {familiar2.edad} - Fecha de nacimiento: {familiar2.fechaDeNacimiento} - E-Mail: {familiar2.email}<br>Tipo: {familiar3.tipo} - Nombre: {familiar3.nombre} - Apellido {familiar3.apellido} - Edad: {familiar3.edad} - Fecha de nacimiento: {familiar3.fechaDeNacimiento} - E-Mail: {familiar3.email}<br>Tipo: {familiar4.tipo} - Nombre: {familiar4.nombre} - Apellido {familiar4.apellido} - Edad: {familiar4.edad} - Fecha de nacimiento: {familiar4.fechaDeNacimiento} - E-Mail: {familiar4.email}<br>Tipo: {familiar5.tipo} - Nombre: {familiar5.nombre} - Apellido {familiar5.apellido} - Edad: {familiar5.edad} - Fecha de nacimiento: {familiar5.fechaDeNacimiento} - E-Mail: {familiar5.email}'
    
    return HttpResponse(documento)


