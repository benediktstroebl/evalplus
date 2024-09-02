
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    a = int(str(n)[:-1])
    b = int(str(n)[-1])
    c = b - 1
    if c >= 0:
        return (10 ** a) - (c * 10 ** a) - (10 ** (a - 1))
    else:
        return 10 ** a - (c * 10 ** a)
