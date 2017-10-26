import random
import numpy
import math





#########MAIN##########

#Returns a randomly weighted matrix
def generate_weights(size):
    weights = []
    for i in xrange(0,size):
        weights.append([float("{0:.1f}".format(random.uniform(-0.5, 0.5))), float("{0:.1f}".format(random.uniform(-0.5, 0.5)))])
    return numpy.asarray(weights)


def step_function(value):
    return 1 if value >= 0 else 0

#FIKS RESULT
def activation(input,weights,threshold):
    dot_product = (input * weights)
    result = []
    err = []
    index = 0
    for x in dot_product:
        result.append(step_function(sum(x)-threshold))
    #result = step_function(result)
    print "result: ", result
    return result

def update_weights(input,weights,learning_rate, error):
    index = 0
    updated_weights = []
    for w in weights:
        updated_weights.append( [w[0] + (input[index][0] * learning_rate * error[index]),
             w[1] + (input[index][1] * learning_rate * error[index])])
        index += 1

    return numpy.asarray(updated_weights)

def toString(output,error,weights):
    print "--------- \n weights: \n", weights, "\n Output: ",output, "\n ----------"

def main(AND_OR):
    #Decides based on input if its using AND or OR as input
    if AND_OR == "AND":
        desired_output = [0,0,0,1]
    elif AND_OR == "OR":
        desired_output = [0,1,1,1]

    input = numpy.array([[0, 0],
                         [0, 1],
                         [1, 0],
                         [1, 1]])

    #Init some variables
    threshold = float("{0:.1f}".format(random.uniform(-0.5, 0.5)))
    #threshold = 0.0
    learning_rate = 0.1
    error = [0,0,0,1]
    timeout = 100
    weights = generate_weights(len(desired_output))
    print "Start weights: \n", weights, "\n"
    print "Threshhold: ", threshold

    while error != [0,0,0,0]:
        output = activation(input,weights,threshold)
        error = [x1 - x2 for (x1, x2) in zip(desired_output, output)]
        weights = update_weights(input,weights,learning_rate,error)
        toString(output,error,weights)
        timeout -= 1

        if timeout == 0:
            raise RuntimeError("Combination of weights and threshold may have caused a deadlock. Program timed out. Initial threshold was: ", threshold)
    print "Finished! Final output: ", output

main("OR")






