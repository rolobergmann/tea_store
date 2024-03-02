from te import Te

# Creación de dos instancias
te_negro = Te()
te_verde = Te()

# Almacenamiento del tipo de dato de cada instancia
tipo_te_negro = type(te_negro)
tipo_te_verde = type(te_verde)

# Impresión del tipo de dato de cada instancia
print(f"Tipo de te_negro: {tipo_te_negro}")
print(f"Tipo de te_verde: {tipo_te_verde}")

# Comparación de tipos de datos
if tipo_te_negro == tipo_te_verde:
  print("Ambos objetos son del mismo tipo")
else:
  print("Los objetos no son del mismo tipo")
