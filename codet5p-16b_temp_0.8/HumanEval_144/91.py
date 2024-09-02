
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    # convert fraction to fraction
    numerator, denominator = [int(i) for i in x.split('/')]
    numerator_new, denominator_new = [int(i) for i in n.split('/')]
    # calculate simplified fraction
    numerator_new, denominator_new = simplify_fraction(numerator, denominator, numerator_new, denominator_new)
    
    if denominator_new == 0:
        return False
    elif denominator == denominator_new:
        return True
    else:
        return False
