def suma(a, b):
    resultado = a + b
    return resultado
class Animal: 
    def __init__(self, patas, tipo_piel):
        self.patas= patas
        self.tipo_piel= tipo_piel
        
class Perro (Animal):
    def __init__(self, raza, patas, tipo_piel):
        self.raza= raza
        super().__init__(patas, tipo_piel)

perro1= Perro("Labrador", 4, "Cuero")
print(perro1.raza)
print(perro1.patas)
print(perro1.tipo_piel)

class Loro(Animal):
    def __init__(self, patas, tipo_piel):
        super().__init__(patas, tipo_piel)
    
    def hablar(self):
        print("ruido de loro")
    
loro1= Loro(2, "plumas")   
loro1.hablar()
