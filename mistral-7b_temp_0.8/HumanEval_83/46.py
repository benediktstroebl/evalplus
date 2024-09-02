
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # this is O(n) complexity
    # return 10**n - 9 * (10**n - 9)
    return 10**n - 9 * 10**(n-1)

