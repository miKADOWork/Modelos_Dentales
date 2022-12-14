

class Modelo:
    def __init__(self, nombre, pacientes_modelos, modelo_cirujia):
        self.caja = nombre
        self.pacientes = pacientes_modelos
        self.disponible = True
        self.tipo = modelo_cirujia


    def isEmpty(self):
        print(self.disponible)


    def PacientesInTheBox(self):
        for key in self.pacientes:
            print(key)
