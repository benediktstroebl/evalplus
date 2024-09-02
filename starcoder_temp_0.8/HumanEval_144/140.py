
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
    x_as_int = int(x)
    n_as_int = int(n)

    x_as_float = float(x)
    n_as_float = float(n)

    simplified_product = x_as_int * n_as_int

    if (x_as_float * n_as_float).is_integer():
        return True
    else:
        return False

