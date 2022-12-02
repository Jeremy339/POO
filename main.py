print("Hola Mundo");

class persona:
    nombre = str
    edad   = int
def _init_(self, nombre, edad):
 self.nombre = nombre
 self.edad   = edad
 
if __name__ == "__main__":
    David= persona("David", 30)
    Elena= persona("Elena", 25)

print(David)
print(Elena)

class MiClase:
    nombre = "Alex"
    edad   =  20
p1 = MiClase()
print(p1.nombre)

class persona2:
    nombre = str
    edad   = int
    genero = str
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad   = edad
        self.genero = genero

p2= persona2("Alex", 20, "Masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero)


class persona3:
    nombre = str
    edad   = int
    genero = str
    estatura = int
    def __init__(self, nombre, edad, genero, estatura):
        self.nombre   = nombre
        self.edad     = edad
        self.genero   = genero
        self.estatura = estatura
    def __str__(self):
        return f"Hola me llamo",{self.nombre}, "tengo", {self.edad},"Mi genero es",{self.genero}, "Mi estatura es",{self.estatura}
    p3 = persona3  ("Juan", 21, "Masculino", 189)
    print(p3)
    
    #Metodos dentro de Objetos
    class Persona4:
        nombre   = str
        semestre = str
        def __init__(self, nombre, semestre):
        self.nombre   = nombre
        self.semestre = semestre
        
    def saludo(self):
        print("Bienvenido "+ self.nombre +" al" + self.semestre)
        
        p4 = Persona4 ("Antonio", "segundo")
        p4.saludo()

        p4.nombre="Jonathan"
        p4.saludo()