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
        cantidadCreados += 1

    def cantidadAsientos(self, asientos):
        totalAsientos = 0
        for unasiento in asientos:
            totalAsientos += 1
        return totalAsientos
    
    def verificarIntegridad(self, registro, asientos):
        b = 1
        for unasiento in asientos:
            if unasiento.registro != self.registro:
                b = 0
        if Motor.registro != self.registro:
            b = 0
        
        if b == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"