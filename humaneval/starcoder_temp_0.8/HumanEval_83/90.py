
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 2
    return 9 * 10 ** (n - 1) + 9 * starts_one_ends(n - 1) + 9 * ends_with_one(n - 1)

