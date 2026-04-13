class Vehiculos:
    def __init__(self,marca,modelo,color,patente,puertas):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.patente=patente
        self.puertas=puertas
        pass
class Moto(Vehiculos):
    def __init__(self, marca, modelo, color, patente, puertas):
        super().__init__(marca, modelo, color, patente, puertas)

class auto(Vehiculos):
    def __init__(self, marca, modelo, color, patente, puertas):
        super().__init__(marca, modelo, color, patente, puertas)