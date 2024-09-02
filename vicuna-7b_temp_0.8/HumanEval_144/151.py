
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
    # Do the simplification of the given expression
    # If the expression is not a valid fraction, return False
    if not (isinstance(x, Fraction) and isinstance(n, Fraction) and n != 0 and n != 1):
        return False

    # Check if the numerator and denominator are not zero
    if (n.numerator == 0 or n.denominator == 0 or x.numerator == 0 or x.denominator == 0):
        return False

    # If the expression is not a valid fraction, return False
    if (n != x or n.denominator != 1 or x.denominator != 1):
        return False

    # Compare the numerators and denominators of both fractions
    return (x.numerator * n.denominator == n.numerator * x.denominator)
