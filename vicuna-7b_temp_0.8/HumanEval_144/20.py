
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
    # Parse x and n
    x, n = map(int, [x, n])

    # Check if n is zero
    if n == 0:
        return False

    # Check if x is zero
    if x == 0:
        return True

    # Check if n is a factor of x
    if n in [i//j for i, j in zip(str(x), str(n)) if j != 0]:
        return True

    # If both x and n are not zero and n is not a factor of x, x\*n is not a whole number
    return False
