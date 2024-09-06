
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
    # n and x are string representation of a fraction, and have the following format,
    # <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    # convert x and n to float
    x = float(x)
    n = float(n)

    # check if n is equal to 0
    if n == 0:
        return False

    # check if n is a factor of x
    if n % x:
        return False

    # check if n is a positive integer
    if int(n) != n:
        return False

    # check if x is a whole number
    if abs(x) == int(x):
        return True

    # check if x is a fraction with n as the denominator
    if n != 1:
        return simplify(x, n // x) and simplify(x, n % x)

    # check if x is a fraction with 1 as the denominator
    return simplify(x, 1) and simplify(n, 1)