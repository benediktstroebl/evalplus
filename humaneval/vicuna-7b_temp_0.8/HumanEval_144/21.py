
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
    # split the string to get the numerator and denominator
    num, den = x.split('/')

    # convert the numerator and denominator to float
    num = float(num)
    den = float(den)

    # check if the denominator is equal to 1
    if den == 1.0:
        return True

    # check if the numerator is a whole number
    if abs(num) % 1 == 0:
        return True

    # check if the denominator is a factor of the numerator
    if abs(num // den) % 1 == 0:
        return True

    # otherwise, return False
    return False