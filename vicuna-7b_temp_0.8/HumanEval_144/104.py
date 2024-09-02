
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
    numerator = int(x[0])
    denominator = int(x[1])
    n_numerator = int(n[0])
    n_denominator = int(n[1])
    if denominator != 0:
        if numerator == denominator or (denominator != 1 and numerator % denominator == 0):
            return False
    if n_denominator != 0:
        if n_numerator == n_denominator or (n_denominator != 1 and n_numerator % n_denominator == 0):
            return False
    if numerator == n_numerator and denominator == n_denominator:
        return True
    return False