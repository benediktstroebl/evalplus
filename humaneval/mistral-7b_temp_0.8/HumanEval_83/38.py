
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 9
    res = 0
    for i in range(1, 10):
        res += starts_one_ends(n - 1)
    if n > 1:
        res *= 10
    res += 10 ** (n - 1)
    return res

