# A python program para mostrar pep8
class automovil:

    # variable de la clase
    ruedas=4

    #constructor de la clase automovil
    def __init__(self,color,modelo,year):
        self.color=color
        self.modelo=modelo
        self.year=year

    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo

    def getYear(self):
        return self.year

    def setColor(self,col):
        self.color=col

    def setModelo(self,Mod):
        self.modelo=Mod

    def setYear(self,yr):
        self.year=yr
        
    # toString como en java
    def toString(self):
        print("Este auto es modelo ",self.modelo,
        "y es de color ",self.color)
#Drive Code
A1=automovil('blanco',2010)
A2=automovil('negro',2020)

A1.toString()
A2.toString()

