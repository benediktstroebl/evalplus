
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
    n = int(n)
    x = int(x)
    t1, t2 = x, n
    if x % n == 0:
        return True
    if x < n:
        while t1 % n:
            t1 = t1 * 10 / n
    if t1 < n:
        return False
    t1 = t1 / n
    t2 = t2 / n
    return t1 == t2
