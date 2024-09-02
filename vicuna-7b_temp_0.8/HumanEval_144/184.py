
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
    # Start by converting x and n to float
    x = float(x)
    n = float(n)
    simplified_x = x.simplify()
    simplified_n = n.simplify()

    # Check if the fraction of x is equal to the numerator and denominator of n is 1
    if simplified_x == simplified_n.numerator // simplified_n.denominator:
        return True
    else:
        return False
