
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
        if (numerator % denominator) == 0:
            return True
        else:
            return False

    if denominator == 2:
        if (numerator % 2) == 0:
            return True
        else:
            return simplify(x[0:2], n[0:2])

    if denominator == 3:
        if (numerator % 3) == 0:
            return True
        else:
            return simplify(x[0:3], n[0:3])

    if denominator == 4:
        if (numerator % 4) == 0:
            return True
        else:
            return simplify(x[0:4], n[0:4])

    if denominator == 5:
        if (numerator % 5) == 0:
            return True
        else:
            return simplify(x[0:5], n[0:5])

    return False