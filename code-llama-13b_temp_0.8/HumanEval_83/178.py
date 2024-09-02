
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    return 9 * 10 ** (n - 2) * 2

