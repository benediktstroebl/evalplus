
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
    # convert x and n to float
    x = float(x)
    n = float(n)

    # check if n is zero
    if n == 0:
        return False

    # check if x and n are valid fractions
    if x <= 0 or not (1 <= int(x) <= 1) or n <= 0 or not (1 <= int(n) <= 1):
        return False

    # check if x is a whole number
    if abs(x - int(x)) == 0.0:
        return True

    # if x is not a whole number, x must be a fraction
    if x != int(x):
        if n % x == 0:
            # if x is a factor of n, return True
            return True

    # if x is not a factor of n, and x != int(x), then x * n is not a whole number
    return False