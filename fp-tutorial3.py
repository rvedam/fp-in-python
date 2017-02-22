#!/usr/bin/python3 -Wall

################################################################################
#
# Lambda Expressions, and closures
#
################################################################################


# example of a simple anonymous function in python
add2 = lambda x: x + 2

print(add2(2))

#
# another way of generating functions with a function
# notice this will create a closure and bind the lambda around a which is
# scoped and bound in the outer function before the lambda is constructed.
#
def create_adder(a):
    return lambda b: a + b

add4 = create_adder(4)
add3 = create_adder(3)

print(add4(4))
print(add3(4))

# old way of creating closures without lambdas
def create_adder_old_way(a):
    def adder(b):
        return a + b
    return adder

add5 = create_adder_old_way(5)

print(add5(6))

# example of function that creates functions
def create_greeter():
    """
    Example of creating a function that creates function with
    inner(scoped) function definitions
    """
    def greeter(x):
        print(x)

    return greeter

a = create_greeter()
b = create_greeter()

a('a is called')
b('b is called')

################################################################################
#
# Itertools overview
#
################################################################################

import itertools

################################################################################
#
# Recursion overview
#
################################################################################

# example of a recursive function that is just a kind of iteration
# compliments of "Functional Programming in Python" by David Mertz

def running_sum(numbers, start=0):
    if len(numbers) == 0:
        print()
        return
    total = numbers[0] + start
    print(total, end=" ")
    running_sum(numbers[1:], total)

running_sum(range(0,11))

# factorial example
def factorial(N):
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N*factorial(N-1)

# clearly this would blow up the stack if we create stack depths > 1000.
# in general this style is discouraged and replaced with a more iterative style
def factorial_iterative(N):
    result = 1
    while N > 1:
        result, N = result*N, N-1
    return result
