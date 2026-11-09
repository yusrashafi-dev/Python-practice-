#class student:
#   name="Yusra"
#   age=22
##object
# student1=student()
#print(f"Name of student:{sudent1.name}")

class student:
    def __init__(self,name, age):
        self.name=name
        self.age=age
student1=student("Yusra",26)
student2=student("Cherop",25)
         
print(student1.name)

#inheriance
class Animal:
    def speak(self):
        print("Dog barking")

        class Dog(Animal):
            def bark(self):
                print("Barking")

        #creating object
        d = Dog()
        d.bark()
        d.speak()
