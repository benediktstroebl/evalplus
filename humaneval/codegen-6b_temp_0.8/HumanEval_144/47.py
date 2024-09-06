
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
    if '/' not in x:
        return False

    numerator, denom = x.split('/')
    numerator = int(numerator)
    denom = int(denom)

    if n.endswith('1'):
        return numerator == 1
    elif n.endswith('2'):
        if denom == 2:
            return numerator/denom == 1
        else:
            return False
    elif n.endswith('3'):
        if denom == 3:
            return numerator/denom == 1
        else:
            return False
    else:
        return False

