
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

    # check if x and n have the same denominator
    if x.denominator != n.denominator:
        return False

    # check if both x and n have a fractional value
    if x.numerator or n.numerator or x.denominator or n.denominator:
        return False

    # convert x and n to integer
    x = int(x)
    n = int(n)

    # check if x and n are both integers
    if abs(x - n) >= 1:
        return True

    # check if x and n are both odd or both even
    if ((x % 2 == 1 and n % 2 == 1) or
        ((x % 2 == 0 and n % 2 == 0) and ((x != n) or abs(x - n) >= 2)))
        return True

    return False
