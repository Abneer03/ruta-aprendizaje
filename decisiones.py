edad = int(input("¿Cuántos años tienes? "))

if edad <= 100 and edad >= 18:
    print("Eres mayor de edad")
elif edad <= 17 and edad >= 13:
    print("Eres adolescente")
elif edad <= 12 and edad >= 0:
    print("Eres menor de edad")
else:
    print("Esa edad no es válida.")
