
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
    if len(x) == 0:
        return True
    if x[-1] == '/':
        x = x[0:-1]
    numerator = int(x[0])
    denominator = int(x[1])
    if numerator == 0:
        return False
    if denominator == 0:
        return False
    if numerator > denominator:
        return False
    if simplify(x, numerator) and simplify(x, denominator):
        return True
    return False

