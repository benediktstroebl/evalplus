
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
    # split the input string into numerator and denominator
    num, den = x.split('/')

    # convert the numerator and denominator to integers
    num = int(num)
    den = int(den)

    # check if the denominator is not zero
    if den == 0:
        return False

    # check if the denominator is a factor of the numerator
    if not gcd(num, den) == 1:
        return False

    # check if the result is a whole number
    result = num / den
    if not isinstance(result, int) or result != result % 1:
        return False

    return True