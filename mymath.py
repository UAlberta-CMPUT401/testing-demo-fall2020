"""
Implementation of methods

DO NOT MODIFY THIS FILE

"""

import random

class MyMath(object):

    # returns a random number
    # NOTE: You do not need to modify this method!
    # Mock it instead
    def bad_random(self):
        file = open('/Users/bob/datafile', 'r')
        numberStrings = file.readlines()
        numbers = [int(x) for x in numberStrings]
        return random.randint(0, len(numberStrings)-1)

    # Test this
    def complicated_function(self, x):
        return self.divide(x), self.bad_random() % 2

    # Test this
    def divide(self, y):
        return self.bad_random() / y

    # Test this
    def abs_plus(self, x):
        return abs(x) + 1
