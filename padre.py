#Herencia en Python
class Persona:
    nombre   = str
    apellido = str

    def __init__(self, nombre, apellido):
     self.nombre   = nombre
     self.apellido = apellido
       
     def imprimir(self):
         print(self.nombre, self.apellido)

x = Persona("Alexander", "Pacho")
x.imprimir()
#Herencia Simple en Python
class Studiante(Persona):
    pass

y = Studiante("Jeremy", "Cañizares")
y.imprimir()

#Agregar atributos a una herencia
class Student(Persona):
    def __init__(self, nombre, apellido, edad):
       Persona.__init__(nombre, apellido)
       self.edad = edad

estudiante1= Student("Carlos", "Daquilema", 25)
estudiante1.imprimir()

#Agregar metodos a una herencia

class Student1(Persona):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
       super().__init__(nombre, apellido)
       self.edad     = edad
       self.semestre = semestre
       
       def bienvenido(self):
           print("Bienvenido " + self.apellido + " al" + self.semestre + " ingresas a los "+self.edad +" años")

p5 =Student1=("Alex", "Pacho", 20, "Segundo")
