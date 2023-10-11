'''
A class is a type
- int is a class
- str is a class
- list is a class
- you get the point!

objects: basically anything that takes up memory
- examples: 3, 'hello', [1,2,3], {'n':0, 'o':1}
- called an INSTANCE of a class
'''

theList = list()
print(type(theList) == list)
theTuple = tuple([1,2,3]) # convert a list to a tuple;
print(f"theList: {theList}, theTuple: {theTuple}");

class Foo:
    def __init__(self, weight, height):
        self.weight = weight 
        self.height = height

theFoo = Foo(0,1)
print(type(theFoo) == Foo)
print(theFoo.weight);
print(theFoo.height);

# Note: named parameters
theOtherFoo = Foo(weight=0, height=1)
print('----------------')




