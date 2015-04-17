from django.shortcuts import render
from models import URLs
from models import NameForm
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django import forms



# Create your views here.
@csrf_exempt  
def MenuInicial(request,recurso):
  formulario = ""
  recurso = request.path_info.split()[0]
  formulario = "<p>404 NOT FOUND</p><p>PAGINA NO ENCONTRADA</p>"
  if request.method == "GET":
    if recurso == "/":
      print "Adios"
      formulario = "<h1>Acortador Web Django </h1><form action='http://localhost:8000/' method='POST' enctype='text/plain'>Introduzca el Valor y pulse Enter: <input type='text' id='url' name = 'url'></form>"
      lista = URLs.objects.all()
      for i in lista:
        formulario += "<div><a href= " 'http://localhost:8000/' + str(i.id) + ">http://localhost:8000/" + str(i.id) + "</a> ----> " + "<a href= " + str(i.larga) + ">" + str(i.larga) + "</a>"
    else:
      print "hola"
      try:
        numero = int(recurso[1:])
        lista = URLs.objects.all()
        for i in lista:
          if(numero == i.id):
            formulario = "<html> <head><html><head><meta http-equiv='Refresh' content='0; url= " + i.larga +"'></head><body></body></html></head><body></body></html>\r\n"
            break
      except:             
        formulario = "<p>404 NOT FOUND</p><p>PAGINA NO ENCONTRADA</p>"
  if request.method == "POST":   
    cuerpo = request.body.split("=",1)[1]
    if not cuerpo.startswith('http'):
      cuerpo = ("http://" + cuerpo[:-2])
    lista = URLs.objects.all()
    try:
      for i in lista:
        print i.larga
        print cuerpo
        if i.larga == cuerpo:
          formulario += "<p>Este Recurso ya esta agregado</p> <a href= " 'http://localhost:8000/'"> http://localhost:8000/</a>"
          return HttpResponse(formulario)
      nuevo = URLs(larga = cuerpo)
      nuevo.save()
      formulario += "<p>Creado el recurso, pruebe en http://localhost:8000/ </p><a href= " 'http://localhost:8000/'"> http://localhost:8000/</a>"
      lista = URLs.objects.filter(larga=cuerpo)
      print lista
    except URLs.DoesNotExist:
      formulario = cuerpo
  return HttpResponse(formulario)




