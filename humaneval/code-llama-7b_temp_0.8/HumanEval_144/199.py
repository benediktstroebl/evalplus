
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

    # split x and n into numerators and denominators
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    # calculate numerator and denominator of simplified fraction
    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)
    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)

    x_simplified_numerator = x_numerator * n_denominator
    x_simplified_denominator = x_denominator * n_numerator

    # check if it is possible to simplify the fraction
    if x_simplified_numerator % x_simplified_denominator == 0:
        return True
    else:
        return False

