
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
    numerator, denominator = map(int, (x[0], n[0]))
    numerator_quo, numerator_rem = divmod(numerator, denominator)
    denominator_quo, denominator_rem = divmod(denominator, denominator)

    if (denominator_quo != 0 and denominator_rem == 0) or (denominator_rem != 0 and denominator_quo == 0):
        return False
    else:
        return True
