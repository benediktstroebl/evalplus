
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return n if n < 10 else n - 1 + starts_one_ends(n - 1)

