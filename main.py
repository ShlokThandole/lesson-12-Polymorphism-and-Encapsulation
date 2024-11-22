class Cat :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a cat. my name is {self.name}. i am {self.age} years old.")

    def make_sound(self):
        print("you cant defeat me")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a dog. my name is {self.name}. i am {self.age} years old.")

    def make_sound(self):
        print("i know but he can")

cat1 = Cat("jake paul", 705)
dog1 = Dog("mike tyson", 199)

for animal in (cat1 , dog1):
    animal.make_sound()
    animal.info()