from abc import ABC, abstractmethod
class ABsclass(ABC):
    def print(self,x):
        print("passed value: ", x)
    @abstractmethod
    def task(self):
        print("we are inside ABsclass task")
class test_class(ABsclass):
    def task(self):
        print("we are inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)
from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
            print("i can walk and run")
class Snake(Animal):
    def move(self):
         print("i can crawl")
class Dog(Animal):
            def move(self):
                print("i can bark")
class Lion(Animal):
            def move(self):
                print("i can roar")
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()

        