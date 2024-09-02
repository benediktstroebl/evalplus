
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
    # convert the string to float and get the numerator and denominator
    num = float(x[:-1])
    den = float(x[-1])

    # check if both are positive
    if num >= 0 and den >= 0:
        # check if the result is a whole number
        if abs(num * den) <= 1:
            return True
        else:
            return False
    else:
        return False
