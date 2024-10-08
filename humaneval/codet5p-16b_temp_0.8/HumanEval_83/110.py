
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    ret = 0
    if n > 0:
        for i in range(0, n+1):
            if len(str(i)) == n and (i % 10 == 1 or i == 1):
                ret += 1
            if len(str(i)) == n and (i % 10 == 1 or i == 10 ** (n - 1)):
                ret += 1
    return ret


