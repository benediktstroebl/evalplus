
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0

    if n == 1:
        return 10

    ones = 1
    zeros = 9
    n -= 2
    while n > 0:
        ones *= 10
        ones += zeros + 1
        zeros *= 9
        n -= 1

    return ones

