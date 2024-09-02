
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
    if not (is_valid_fraction(x) and is_valid_fraction(n)):
        return False
    numerator = int(x.numerator)
    denominator = int(x.denominator)
    n_numerator = int(n.numerator)
    n_denominator = int(n.denominator)
    if denominator == 0:
        return False
    if (numerator == 0 or n_numerator == 0) and (denominator != 1 and n_denominator != 1):
        return False
    if (numerator == n_numerator and denominator == n_denominator) or (denominator == 1 and n_denominator == 1):
        return True
    return False
