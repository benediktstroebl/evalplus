
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
    # Check if x and n are equal
    if x == n:
        return True

    # Split x and n into their numerator and denominator
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    # Check if the numerator of x and n are equal
    if x_numerator != n_numerator:
        return False

    # Check if the denominator of x and n are equal
    if x_denominator != n_denominator:
        return False

    # If numerator and denominator are equal, return True
    return True