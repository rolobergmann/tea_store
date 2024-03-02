class Te:
  # Atributo de clase: Duración
  duracion = 365

  # Método estático para obtener tiempo de preparación y recomendación
  @staticmethod
  def obtener_preparacion(sabor):
    tiempos = {
      1: 3,
      2: 5,
      3: 6
    }
    recomendaciones = {
      1: "Desayuno",
      2: "Medio día",
      3: "Atardecer"
    }
    return tiempos[sabor], recomendaciones[sabor]

  # Método estático para obtener precio
  @staticmethod
  def obtener_precio(formato):
    precios = {
      300: 3000,
      500: 5000
    }
    return precios[formato]
  
  def obtener_sabor_texto(self, sabor):
        sabores = {
            1: "Negro",
            2: "Verde",
            3: "Hierbas"
        }
        return sabores[sabor]
