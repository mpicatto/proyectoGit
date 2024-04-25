def resta(a,b):
    resultado = a - b
    return resultado #devulve el resultado

#herencias
class Animal:
    def __init__(self,patas,tipo_piel):
        self.patas = patas
        self.tipo_piel= tipo_piel

class Perro(Animal):
    def __init__(self,raza,patas,tipo_piel):
        super().__init__(patas,tipo_piel)
        self.raza = raza


perro1 = Perro("Labrador", 4, "pelos")
print(perro1.patas)



class Loro(Animal):
    def __init__(self,patas,tipo_piel):
        super().__init__(patas,tipo_piel)
    def hablar(self):
        print("ruido de loro")

loro1 = Loro(2,"plumas")
loro1.hablar()
