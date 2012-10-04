import random
import itertools
import math

def generate_expressions(numbers):
    
    for a, b, c, d, e in itertools.permutations(numbers):
        for k, l, m, n in itertools.product(*([['+', '-', '*', '/']] * 4)):
            yield '%f %s %f %s %f %s %f %s %f' % (a, k, b, l, c, m, d, n, e)



def main():
    BigNum = 2
    OtrNum = 3
    print "How many Big num?"
    BigNum = int(raw_input("= "))
    OtrNum = 5 - BigNum


    numbers = (
        [random.randrange(1, 11) for i in xrange(OtrNum)]
        +[random.choice([25,50,75,100]) for i in xrange(BigNum)]
    )
    target = random.randrange(100, 1000)

    #    closeness(eval(generate_expression(numbers)), target)

    print "Numbers" ,numbers
    print "Target", target

    results = []
    best = target
    bestexp = ""
    for i in generate_expressions(numbers):
	try:
            guess = eval(i)
        except ZeroDivisionError:
            continue

	if math.trunc(guess) != guess:
            continue

        diff = abs(guess - target)
        if diff < best:
	    best = diff      
            bestexpr = i
        #print '%s = %s' % (i, guess)
    print "\n\n"
    print bestexpr, "=", target, "difference = ", int(best) 

if __name__ == '__main__':
    main()
    
