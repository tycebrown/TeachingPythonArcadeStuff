'''
A class is a type
- int is a class
- str is a class
- list is a class
- you get the point!

objects: basically anything that takes up memory
- examples: 3, 'hello', [1,2,3], {'n':0, 'o':1}
- called an INSTANCE of a class

To create an object (generally):
- typeOfObject(arguments, ...);
- like a function call (called a constructor)
- examples:
  - list() #creates empty list
  - Square(10) #creates a square with a side lenght of 10 (going to make 10x10 square)
'''


# make a class; call it Cat
# Cat('winchester', 13)

class Square:
    def __init__(self, length):
        self.length = length;

theSquare = Square(10);

class Car:
    def __init__(self, speed, color):
        self.speed = speed;
        self.color = color;

chevy = Car(69, 'red');

class Cat: 
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

theCat = Cat('winchester', 13)
print(theCat.name);
print(theCat.age);











