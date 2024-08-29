# built-in function for display output in python print()
print("Hello DevSecOps X CyberSecurity X Spring Microservice")

# class concept in python
class Piglet:
    def speak(self):
        print("oink oink")

class Person:
    def __init__(self, name, age, subject):
        self.name=name
        self.age=age
        self.subject=subject
    def showinfo(self):
        print("Student name is {}\nAge is {} years old\nSubject is {}".format(self.name, self.age, self.subject))

student1 = Person("Sokny",16,"DevSecOps")
student1.showinfo()
student2 = Person("Makara",32,"DevSecOps")
student2.showinfo()

# different between sort and sorted built-in function in python
list1 = [5,2,8,9,4]
list2 = sorted(list1)
print(list1)
print(list2)






