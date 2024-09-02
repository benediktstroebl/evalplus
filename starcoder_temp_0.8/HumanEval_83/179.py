
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return int((9 * 10 ** (n - 1) + 1) / 10) + int((9 * 10 ** n + 1) / 10)
