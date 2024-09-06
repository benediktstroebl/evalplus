
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
    # split x and n to numerator and denominator
    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    # convert x and n to float
    x_float = float(x_numerator) / float(x_denominator)
    n_float = float(n_numerator) / float(n_denominator)

    # check if both x and n have zero as denominator
    if x_denominator == 0 or n_denominator == 0:
        return False

    # check if both x and n are equal
    if x_float == n_float:
        return True

    # check if both x and n are integers
    if x_float.is_integer() and n_float.is_integer():
        if x_float.int() * n_float.int() == x_float.int():
            return True

    # check if x and n have the same denominator
    if abs(x_denominator - n_denominator) > 1e-6:
        return False

    # check if x is divisible by n
    if x_float % n_float != 0:
        return False

    # check if n is divisible by x
    if n_float % x_float != 0:
        return False

    return True