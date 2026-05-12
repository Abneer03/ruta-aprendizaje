#Diccionarios

Uno = {
    "nombre" : "Tony",
    "edad" : 15,
    "sexo" : "Masculino" ,
    "color" : "Azul"}

Dos = {
    "nombre": "Aurora",
    "edad": 36 ,
    "sexo": "Femenino",
    "color": "Azul"}

Tres = {
    "nombre": "Abneer",
    "edad": 20,
    "sexo": "Masculino",
    "color" : "Negro"}

Sujetos = [Uno, Dos, Tres]

for Sujeto in Sujetos:
    print(Sujeto["nombre"])
    print(Sujeto["edad"])
    print(Sujeto["sexo"])
    print(Sujeto["color"])
        