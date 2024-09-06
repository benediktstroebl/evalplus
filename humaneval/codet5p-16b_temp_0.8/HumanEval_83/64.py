
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 0: return 0

    if n == 1: return 2

    if n == 2: return 10

    return 2 * (9**(n-2)) + 2 * starts_one_ends(n-1)
