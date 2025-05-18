##Actividad 2 
##Cachiripun

Opciones =["piedra", "papel" , "tijeras"]
humano = input("Elige piedra, papel o tijeras: ").lower()

while True:
    if humano not in Opciones:
        humano = input("Tu elección debe limitarse a piedra, papel o tijeras: ").lower()
    else:
        print("Buena elección!!!")
        break

import random as r
maquina = r.choice(Opciones)
print(f"La decisión del computador fue: {maquina}")

if humano == maquina:
    resultado = "Empate"
elif (humano == "tijera" and maquina == "papel") or \
     (humano == "papel" and maquina == "piedra") or \
     (humano == "piedra" and maquina == "tijera"):
    resultado = "Ganaste!!!"
else:
    resultado = "Perdiste :("

print(f"Tú elegiste: {humano}")
print(f"Computador eligió: {maquina}")
print(f"El resultado fue: {resultado}")