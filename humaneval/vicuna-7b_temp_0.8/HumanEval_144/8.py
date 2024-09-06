
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
    # Check if both x and n are not zero
    if (x.numerator != 0 and x.denominator != 0) and (n.numerator != 0 and n.denominator != 0):
        # Get numerator and denominator of x and n
        numerator = x.numerator
        denominator = x.denominator
        nnumerator = n.numerator
        ndenominator = n.denominator
        # Check if x is a multiple of n
        if x == int(x) % n:
            return True
        # Check if n is a multiple of x
        if n == int(n) % x:
            return True
        # Check if x and n are not relatively prime
        if not gcd(x, n) == 1:
            return False
    return False
