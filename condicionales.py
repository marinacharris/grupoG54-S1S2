#Realice un programa que lea un número entero y diga si es mayor o igual a 100
respuesta = "S" #= es un operador de asignación
while respuesta == "S": #== es un operador de comparación
    numero = int(input("Digite un número entero:\n")) #int convierte a entero, str conviete a string o cadena de caracteres
    if numero >= 100:
        print('El número',numero,'es mayor o igual a 100')
    else:
        print(f"El número {numero} es menor a 100") #f-strings
    respuesta = input('Presione "S" para continuar o cualquier letra para salir\n')