import random
import numpy
import math

input = numpy.array([[0,0],
                           [0,1],
                           [1,0],
                           [1,1]])

threshold = random.uniform(-0.5, 0.5)

#TODO randomize weight values
weights = numpy.array([[0.3,-0.1],
                       [0.3,-0.1],
                       [0.3,-0.1],
                       [0.2,-0.1]])

def step_function(value):
    return 0 if value < 0 else 1



test = (input * weights)
print test

output = []

for x in test:
    print step_function((x[0]+x[1]) - 0.2)


#def main(input):











