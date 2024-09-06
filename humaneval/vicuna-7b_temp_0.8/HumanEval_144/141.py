
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

    if denominator == 0:
        return False
    if denominator == 1:
        return (numerator == n_numerator and x[2] == n[2]) or (numerator == n_denominator and x[2] == n[3])
    if denominator > 1:
        if (numerator % denominator == 0 and denominator != 1) or (n_numerator % n_denominator == 0 and n_denominator != 1):
            return False
    return True
