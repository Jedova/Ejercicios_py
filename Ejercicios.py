##Actividad IMC
## Clasificación OMS
W = float(input("ingresa tu peso en [kg]: "))
H = float(input ("ingresa tu altura [m]: "))
IMC = W/H**2

Resultado = print (f"Su resultado de IMC es: {IMC:.2f}") 

if IMC < 18.5:
    calificación_OMS = "Bajo peso"
elif IMC >= 18.5 and IMC < 25:
    calificación_OMS = "Adecuado"
elif IMC >= 25 and IMC < 30:
    calificación_OMS = "Sobrepeso"
elif IMC >= 30 and IMC < 35:
    calificación_OMS = "Obesidad Grado I"
elif IMC >= 35 and IMC < 40:
    calificación_OMS = "Obesidad Grado II"
else: 
    calificación_OMS = "Obesidad Grado III"

print(f"clasificación conforme la OMS:{calificación_OMS}")