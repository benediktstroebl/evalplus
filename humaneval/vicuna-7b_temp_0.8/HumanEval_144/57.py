
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
    numerator = int(x[0])
    denominator = int(x[1])
    y = int(n[0])
    m = int(n[1])

    if denominator == 0:
        return False

    if denominator == 1:
        if (y * numerator == m):
            return True
        return False

    if numerator == 0:
        return False

    if y * numerator == m:
        return True
    if y * numerator == m - denominator:
        return True

    if y * (numerator - 1) + m // 2 == m:
        return True

    if y * (numerator - 1) + m // 2 == m - 1:
        return True

    if y // m == (numerator - 1) // denominator + 1:
        return True

    return False