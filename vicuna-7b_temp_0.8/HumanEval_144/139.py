
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
    # Convert x and n to Fraction objects
    x = Fraction(x)
    n = Fraction(n)

    # Check if the denominator of x and n is not zero
    if n.denominator != 1:
        return False

    # Check if the numerator of x and n is not zero
    if x.numerator != 1:
        return False

    # Check if n is a factor of x
    if n != 1 and x.is_ratio(n) and n != x:
        return True

    # Check if x is a factor of n
    if n != 1 and n.is_ratio(x) and n != x:
        return True

    # If x and n have no common factors and are not factors of each other, they are simple fractions
    # and their product will be a whole number.
    return x.numerator * n.denominator == x.denominator * n.numerator