print("CALCULADORA IVA") # CALCULADORA IVA es un programa para calcular el precio de un producto con el IVA
cliente = input("¿Cúal es tu nombre? ") # El cliente debe ingresar su nombre para registrar el cálculo
precio_sin_iva = float(input("Introducir precio sin IVA: ")) # El cliente debe ingresar el precio neto del producto sin IVA
porcentaje_iva = int(input("Introducir el porcentaje de IVA: ")) # El cliente debe ingresar el porcentaje de IVA que desea sumarle al precio neto del producto
IVA = precio_sin_iva * porcentaje_iva/100 # Ecuación para calcular el IVA  del precio neto del producto

for _ in cliente:
    print(f"Cálculo realizado por {_}")
    print(f"Precio sin IVA: {precio_sin_iva} euros")
    print(f"IVA: {IVA} euros")
    print(f"Precio con IVA: {precio_sin_iva +  IVA} euros")

# Historico de datos ingresados por clientes utilizando el programa
print("HISTORICO DE DATOS INTRODUCIDOS POR CLIENTES")
historico_precio = [45, 50, 20]
historico_nombre = ["Maria", "Luisa", "Ana"]
print(f"{historico_nombre} hicieron cálculos con: {historico_precio} euros respectivamente") 
# MEJORAS: se requiere mejorar la presentación de los datos del historico de una forma más ordenada


# Como un usuario que no sabe calcular el valor del IVA de un precio
# Quiero una calculadora de IVA 
# Para que haga el cálculo del valor del IVA y el precio total con IVA, conociendo el precio sin IVA y el porcentaje de IVA








