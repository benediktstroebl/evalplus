
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
    # check if x and n are valid fractions
    if not (is_valid_fraction(x) and is_valid_fraction(n)):
        return False

    # check if the denominator of n is zero
    if n[0] == '0':
        return False

    # check if the denominator of x is zero
    if x[0] == '0':
        return False

    # check if the numerator of x and n are coprime
    if gcd(int(x[1:]), int(n[1:])) != 1:
        return False

    # check if x and n are a valid fraction
    if int(x) != int(n) or int(x) not in fractions:
        return False

    # perform the multiplication
    y = int(x) * int(n)

    # check if y is a whole number
    if y % 1 != 0:
        return False

    return True
