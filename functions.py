################################################################################
#
# Callables
#
################################################################################

import functools, operator

# on top of named functions and lambdas one can create classes that are Callable
# exmaple of an Adder class that is Callable

class Adder:
    def __init__(self, x):
        self.x = x
    def __call__(self, b):
        return self.x + b

add4 = Adder(4)
print add4(4)

# compare this with what you would do with normal generating function
def make_adder(a):
    def adder(b):
        return a + b
    return adder

add4_f = make_adder(4)
print add4_f(4)

# both look equivalent but there is a little gotcha with the Adder class (can you see what it is)

# example of using class methods in Python
class Math(object):
    @staticmethod
    def product(*nums):
        return functools.reduce(operator.mul, nums)
    @staticmethod
    def power_chain(*nums):
        return functools.reduce(operator.pow, nums)
