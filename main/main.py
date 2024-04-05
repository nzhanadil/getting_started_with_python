# printing
# print('hello, world!')

# variables types
# def variables():
#     a = 28  # int
#     b = 1.5  # float
#     c = "Hello!"  # str
#     d = True  # bool
#     e = None  # NoneType

# def greet():
#     # getting input from user
#     name = input("Name: ")
#     # print("Hello, " + name + '!')
#     print(f"Hello, {name}!")
# greet()

# def conditions():
#     n = int(input("Number: "))
#     if n > 0:
#         print("number is positive")
#     elif n < 0:
#         print("number is negative")
#     else:
#         print("number is zero")
# conditions()

# def sequences():
#     name = "Harry"
#     print(name[2])
# sequences()

# def data_structures():
#     n = 'f'
#     # list - sequence of mutable values
#     # tuple - sequence of immutable values
#     # set - collection of unique values
#     # dict - collection of key-value pairs

# def list():
#     names = ["Harry", 'Ron', "Hermione", 'Ginny']
#     names.append("Draco")
#     names.sort()
#     print(names)
# list()

# def set_test():
#     s = set()
#     s.add(1)
#     s.add(2)
#     s.add(3)
#     s.add(1)
#     s.add(4)
#
#     s.remove(3)
#     print(s)
#     print('set length:', len(s))
# set_test()

# def loops():
#     for i in range(1, 5):
#         print(i)
#
#     names = ["Harry", 'Ron', "Hermione", 'Ginny']
#     for name in names:
#         print(name)
# loops()

# def dictionary():
#     d = {"1": "one", "2": "two"}
#     d["3"] = "three"
#     print(d)
# dictionary()

# def square(x):
#     return x*x
#
# print(square(5))

# from class_name import def_name

# classes

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p = Point(2, 5)
# print(p.x)
# print(p.y)

# class Flight:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
#
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
#
#
# flight = Flight(3)
#
# people = ["A", "B", "C", "D"]
#
# for person in people:
#     success = flight.add_passenger(person)
#     if success:
#         print(f"Person {person} added to flight!")
#     else:
#         print(f"No available seats for {person}!")


