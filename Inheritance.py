class Employee:
    salary=2000
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def show_information(self):
        return "Ad: {}    Soyad: {}".format(self.name,self.surname)

class Programist(Employee):
    salary=2900
    def __init__(self,name,surname,language):
        super().__init__(name,surname)
        self.language=language
    def show_information(self):
        return "Ad: {}    Soyad: {}    Dil: {}".format(self.name,self.surname,self.language)

class Designer(Employee):
    def __init__(self,name,surname,proqram):
        super().__init__(name,surname)
        self.proqram=proqram

    def show_information(self):
        return "Ad: {}    Soyad: {}    Proqram: {}".format(self.name,self.surname,self.proqram)

employee1=Employee("Maria","Curie")
employee2=Employee("Isaac","Newton")

programist1=Programist("Guido Van","Rossum","Python")
programist2=Programist("James","Gosling","Java")

print(employee1.salary)
print(programist1.salary)
print(employee2.show_information())
print(programist2.show_information())

designer1=Designer("Aytan","Quluyeva","Figma")
designer2=Designer("Fidan","Mirza","UX/UI")
print(designer2.name)
print(designer2.salary)



