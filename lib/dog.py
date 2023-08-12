#!/usr/bin/env python3
# 1. Add method `sit()` to `Dog` class that will print
# "The dog is sitting."

class Dog:
    # Class body goes here
    # Instance method definition
    def sit(self):
        print('The dog is sitting.')

    def bark(self):
        print('Woof!')


spot = Dog()
spot.sit()
