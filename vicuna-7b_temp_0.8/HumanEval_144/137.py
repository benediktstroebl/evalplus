
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
    # convert x and n to float
    x = float(x)
    n = float(n)

    # check if x and n have a common denominator
    gcd = abs(x / n)
    if gcd != 1:
        return False

    # if x and n have a common denominator, simplify the expression
    simplified = float(x * n)
    if simplified == int(simplified):
        return True
    else:
        return False
