
# from https://docs.python.org/3.9/tutorial/classes.html

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass ()
print (x.f ())


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
