
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        raise ValueError('Input n must be positive')
    return 9 * 10 ** (n - 2) * 2
