
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        s = 1
        for i in range(n-1):
            s += 9 * (10**i)
        return s + (10**(n-1)) + starts_one_ends(n-1)
