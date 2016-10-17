#!/usr/bin/python -Wall

#################################################################################
#
# Comprehensions
#
################################################################################
import itertools

# list comprehensions example
evens = [x for x in range(0, 11) if x % 2 == 0]
print evens

# example of dictionary comprehensions
ordinals = {(65+i):chr(65+i) for i in range(6)}
print ordinals

# example of set comprehensions
aset = {i for i in ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'G']}
print aset

# Generator comprehensions
#
# Generator comprehensions look like List comprehensions, but do not need square
# brackets around them (in some contexts though parentheses are required)
# Generator comprehensions lend

# example: reading in some data
f = open('demo-data.txt', 'r')

# the following does not evaluate, rather the syntax tells Python to create a
# generator based on the comprehension expression that follows, which in this case
# just delays reading the file. The returned object is iterable and is lazily-evaluated.
log_lines = (line for line in f)

# you can now iterate through the collection
# TODO: there is a better way of doing this. left as an exercise to the reader
first_5_lines = list()
for x in range(5):
    first_5_lines.append(log_lines.next())
print first_5_lines
