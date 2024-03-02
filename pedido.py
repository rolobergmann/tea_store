from te import Te

# Solicitud de datos al usuario
while True:
    try:
        sabor = int(input("Ingrese el sabor del té (1: Negro, 2: Verde, 3: Hierbas): "))
        if 1 <= sabor <= 3:
            break
        print("Sabor no válido. Ingrese un valor entre 1 y 3.")
    except ValueError:
       print("Entrada inválida. Ingrese un número entero entre 1 y 3.")

while True:
    try:
        formato = int(input("Ingrese el formato del té (300gr o 500gr): "))
        if formato in (300, 500):
            break
        print("Formato no válido. Ingrese 300 para 300gr o 500 para 500gr.")
    except ValueError:
        print("Formato no válido. Ingrese 300 para 300gr o 500 para 500gr.")


# Creación de una instancia de la clase Te
te = Te() 

# Obtención de información del té
tiempo, recomendacion = te.obtener_preparacion(sabor)  
precio = te.obtener_precio(formato)

# Impresión del detalle del pedido
print(f"--- Detalle del pedido ---")
print(f"Sabor: {te.obtener_sabor_texto(sabor)}") # ¡Usa la instancia 'te'!
print(f"Formato: {formato}gr")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")


