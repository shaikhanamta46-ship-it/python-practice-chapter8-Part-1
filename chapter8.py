#chapter 8 (oops in python - object oriented programming..
#class - blueprint for creating objects
class student:
    college_name = "ABC college.." #object attribute defined
 
    def __init__(self):
        self.name = "anam"
        self.age = 20
        self.marks = 90
s1 = student() #object of the class student
print(s1.name) #accessing the name attribute of the object s1
print(s1.age) #accessing the age attribute of the object s1
print(s1.marks) #accessing the marks attribute of the object s1
print(s1.college_name)

class car:
    color = "blue"
    brand = "BMW"

c1 = car()#object of the class car
print(c1.color)
print(c1.brand)

#LET'S use constructor __init__ to iniatilize the attributes of the class
# class car:
#     def __init__(self): #self is the parameter which refers to current object of the class
#         self.color = "blue"
#         self.brand = "BMW"

# c1 = car()
# print(c1.color)
# print(c1.brand)

#lets make new class
#paramitized constructor
class student:
     def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

        print("adding new student using database")
s1 = student("Karan",90)
print(s1.name)
print(s1.marks)
s2 = student("Arjun",89)
print(s2.name)
print(s2.marks)

# #default costructor

# class remedie:
#     def __init__(self):
#         print("adding new student")

#class and instance attributes
class student2:
    college_name = "jecrc"
    name1 = "autonomous"

    def __init__(self, name1, marks):
        self.name1 = "anam"#object attr>class atrr
        self.marks = marks

    def welcome(self):
        print("welcome student",self.name1)
    
    def get_marks(self):
        return self.marks

    
       

s1 = student2("karan",197)
s1.welcome()
print(s1.name1)
print(student2.college_name)
print(s1.get_marks())

#lets practice question1


class student4:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    @staticmethod
    def hello():
            print("hello")



    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your avg score is:", sum/3)
        
        
s1 = student4("anamta shaikh",[98,99,89])
s1.get_avg()
s1.hello()

#abstraction- show only imp things internal things hide

class Car:
    def __init__(self):
       self.acc = False
       self.brk = False
       self.clutch = False

    def start(self):
         self.clutch = True
         self.acc = True
         print("car started")

car1 = Car()
car1.start()