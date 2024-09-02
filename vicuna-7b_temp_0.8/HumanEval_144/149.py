
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
    # convert x, n to float
    x = float(x)
    n = float(n)

    # if x or n is zero, return False
    if x == 0.0 or n == 0.0:
        return False

    # calculate gcd(x,n)
    gcd = abs(n)
    if gcd != 1:
        gcd = gcd % 1
    x = x % gcd
    n = n % gcd

    # if gcd is not 1, return False
    if gcd != 1:
        return False

    # if x and n have the same sign, return False
    if x != 0.0 and n != 0.0:
        return False

    # if x and n have different signs, simplify and return True
    if x < 0.0 and n > 0.0:
        n = -n
        return simplify(x, n)
    elif x > 0.0 and n < 0.0:
        x = -x
        return simplify(x, n)

    return True