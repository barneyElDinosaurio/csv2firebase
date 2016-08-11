# -*- coding: utf-8 -*-

#IMPORTANDO LIBRERIAS
import csv
import json
from firebase import firebase

#mi objeto de firebase
firebase = firebase.FirebaseApplication('https://shiftdeveloperchallenge.firebaseio.com/', None)

     
data = []#array
#LEYENDO INFO DEL CSV 
with open('cloudChallenge.csv') as cvsfile:#capturando archivo csv
	read = csv.reader(cvsfile)
	for row in read:#leyendo todas las filas
	  nombre = row[0].lower()
	  nota1 = int(row[1])
	  nota2 = int(row[2])
	  nota3 = int(row[3])
	  personality = row[4].lower()
	  nota4 = int(row[5])
	  ejecucion = int(row[6])
	  correo = row[7]
	  ciudad = row[8]
	  github = row[9]
	  video = row[10]
	  #firebase.post('/angular',nombre)#crear id unico

#SUBIENDO INFO A MI BASE DE DATOS EN FIREBASE
	  firebase.put('/cloud/'+nombre,'informacion personal',{'personalidad': personality,'correo': correo,'ciudad': ciudad,'github': github,'video': video})
	  firebase.put('/cloud/'+nombre,'notas',{'nota1': nota1,'nota2': nota2,'nota3': nota3,'nota4': nota4,'ejecucion': ejecucion})
	 
