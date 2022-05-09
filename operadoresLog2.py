




edad = int(input("Digite su edad:\n"))
ingresos = int(input("Ingrese sus ingresos anuales sin puntos ni comas:\n"))
if ingresos < 50831000 or edad < 18:
    print("Usted no debe presentar la declaración de renta")
else:
    print("Usted debe presentar la declaración de renta")
    