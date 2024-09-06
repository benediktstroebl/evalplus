
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
    # split x and n
    x, n = list(map(int, [x, n]))

    # check if x and n are equal to 0
    if x == 0 and n != 0:
        return False

    # check if n is 0
    if n == 0:
        return True

    # convert x and n to integer if it can't be converted return False
    try:
        x = int(x)
    except ValueError:
        return False

    try:
        n = int(n)
    except ValueError:
        return False

    # check if n divides x
    if n % x == 0:
        return True

    # if not, check if n is the only divisor
    for d in range(2, int(n**2) + 1):
        if n % d == 0:
            return True

    return False