
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # subtract 1s that start with 0
    num_ones = 9 * 10 ** (n - 1)
    # subtract 1s that end with 0
    if n > 1:
        num_ones -= 10 ** (n - 1)
    return 10 ** n - num_ones

