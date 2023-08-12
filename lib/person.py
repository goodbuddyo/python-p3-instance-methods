#!/usr/bin/env python3
# 2. Define a `Person` class in `lib/person.py`
# 3. Add an instance method `talk()` to your Person class that will print "Hello World!"
# 4. Add an instance method `walk()` to your Person class that will print "The person is walking."
class Person:
    # Class body goes here
    # Instance method definition
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


joe = Person()
joe.talk()
