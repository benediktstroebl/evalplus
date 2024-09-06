
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
    if n.startswith("1") and x.startswith("1"):
        return True
    elif n.startswith("2") and x.startswith("2"):
        return False
    else:
        n_numerator = int(n[1:])
        x_numerator = int(x[1:])
        n_denominator = int(n[:-1])
        x_denominator = int(x[:-1])
        if n_numerator == 0 and x_denominator == 0:
            return False
        if n_denominator == 0:
            return True
        if x_numerator == 0:
            return False
        if n_numerator == 1 and n_denominator == 1 and x_numerator == 1 and x_denominator == 1:
            return True
        if n_numerator == 2 and n_denominator == 2 and x_numerator == 2 and x_denominator == 2:
            return True
        if n_numerator == 3 and n_denominator == 3 and x_numerator == 3 and x_denominator == 3:
            return True
        if n_numerator == 4 and n_denominator == 4 and x_numerator == 4 and x_denominator == 4:
            return True
        if n_numerator == 5 and n_denominator == 5 and x_numerator == 5 and x_denominator == 5:
            return True
        if n_numerator == 6 and n_denominator == 6 and x_numerator == 6 and x_denominator == 6:
            return True
        if n_numerator == 7 and n_denominator == 7 and x_numerator == 7 and x_denominator == 7:
            return True
        if n_numerator == 8 and n_denominator == 8 and x_numerator == 8 and x_denominator == 8:
            return True
        return False