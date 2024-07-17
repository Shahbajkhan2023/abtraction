

# class Test:

#     @abstractmethod
#     def m1(self):
#         pass 



# from abc import *

# class Test:

#     @abstractmethod
#     def m1(self):
#         pass

# c = Test()






# from abc import *

# class Test:
#     pass 


# t = Test()




# from abc import *

# class Test(ABC):
#     pass 

# t = Test()




# from abc import *


# class Test(ABC):

#     @abstractmethod
#     def m1(self):
#         pass


# c = Test()




# from abc import *

# class Test:

#     @abstractmethod
#     def m1(self):
#         print('Hello')

# t = Test()
# t.m1()




# from abc import *

# class Test(ABC):

#     @abstractmethod
#     def m1(self):
#         pass

# class Test1(Test):
#     pass 




# from abc import *

# class Vehicle(ABC):
    
#     @abstractmethod
#     def no_of_wheels(self):
#         pass


# class Bus(Vehicle):
#     pass


# b = Bus()



# from abc import *

# class Vehicle(ABC):
#     @abstractmethod
#     def no_of_wheels(self):
#         pass


# class Bus(Vehicle):
#     def no_of_wheels(self):
#         return 12
    
# class Auto(Vehicle):
#     def no_of_wheels(self):
#         return 4
    

# b = Bus()
# print(b.no_of_wheels())


# a = Auto()
# print(a.no_of_wheels())




# from abc import *

# class DatabaseInterface(ABC):
#     @abstractmethod
#     def connected(self):
#         pass

#     @abstractmethod
#     def disconnected(self):
#         pass


# class Oracle(DatabaseInterface):
#     def connected(self):
#         print('Connecting to oracle database...')

#     def disconnected(self):
#         print('Disconnecting to the oracle database...')


# class Sybase(DatabaseInterface):
#     def connected(self):
#         print('Conneting to sybase database...')

#     def disconnected(self):
#         print('Disconnecting to the sybase database....')



# dbname = input('Enter Database Name: ')
# classname = globals()[dbname]
# x = classname()
# x.connected()
# x.disconnected()



# from abc import *


# class Vehicle(ABC):
#     @abstractmethod
#     def no_of_wheels(self):
#         pass



from abc import *

# abstract base class for Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'Roar!'
    
    def eat(self):
        return 'Lion is eating meat.'
    

class Elephant(Animal):
    def make_sound(self):
        return 'Trumpet!'
    
    def eat(self):
        return 'Elephant is eating leaves and grass.'
    


class ZooKepeer:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}: {animal.eat()}"
    
    def perform_health_check(self, animal):
        return f"{self.name} is checking health of {animal.name}"
    
    def observe_sound(self, animal):
        return f"{self.name} hears {animal.name} making sound: {animal.make_sound()}"
    

def main():
    lion = Lion('Simba')
    elephant = Elephant('Dumbo')

    zookepeer = ZooKepeer('Jhon')
    print(zookepeer.feed_animal(lion))
    print(zookepeer.perform_health_check(lion))
    print(zookepeer.observe_sound(lion))


    print(zookepeer.feed_animal(elephant))
    print(zookepeer.perform_health_check(elephant))
    print(zookepeer.observe_sound(elephant))


if __name__ == "__main__":
    main()