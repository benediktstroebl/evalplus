
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
    # Check the numerator and denominator of x and n
    if x.numerator == 0 or x.denominator == 0 or n.numerator == 0 or n.denominator == 0:
        return False

    # check the sign of x and n
    if x.numerator > 0 and n.numerator > 0 or \
       x.numerator < 0 and n.numerator < 0 or \
       x.denominator > 0 and n.denominator > 0 or \
       x.denominator < 0 and n.denominator < 0:
        return False

    # check if the expression is a whole number
    if x.numerator * n.denominator == int(x * n):
        return True

    return False