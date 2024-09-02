
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
    if n == "":
        return True
    else:
        x_numerator = int(x[0:len(x) - 2])
        x_denominator = int(x[len(x) - 2:])
        n_numerator = int(n[0:len(n) - 2])
        n_denominator = int(n[len(n) - 2:])
        if (n_numerator / n_denominator) >= x_numerator / x_denominator:
            return False
        else:
            return True
