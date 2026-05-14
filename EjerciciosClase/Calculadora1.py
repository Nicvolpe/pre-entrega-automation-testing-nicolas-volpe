nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
profesion = input("Introduce tu profesión: ")

num1 = float(input("Introduce el primer número:"))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")



def suma(num1, num2):
    return num1 + num2

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2
else:
    resultado = "Operación inválida"

print(f"El usuario {nombre} de {edad} años y profesión {profesion} tiene como resultado: {resultado}")