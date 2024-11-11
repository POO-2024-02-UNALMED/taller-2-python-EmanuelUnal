class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        lisColores = ["rojo","verde","amarillo","negro","blanco"]
        if nuevoColor in lisColores:
            self.color = nuevoColor
        
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro
    
    def asignarTipo(self, nuevoTipo):
        tipolist = ["electrico", "gasolina"]
        if nuevoTipo in tipolist:
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asientos:
            if asiento is not None:
                totalAsientos += 1
        return totalAsientos
    
    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento and asiento.registro != self.registro:
                return "Las piezas no son originales"
        
        if self.motor and self.motor.registro != self.registro:
            return "Las piezas no son originales"
        
        return "Auto original"
