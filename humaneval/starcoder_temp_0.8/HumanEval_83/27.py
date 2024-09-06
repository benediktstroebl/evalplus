
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return int(n > 1 and (n - 1) * (10 ** (n - 2)) + 1)
