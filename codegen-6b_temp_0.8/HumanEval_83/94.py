
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 0

    return (n-1) * (9 * n * n + 9 * n - 2) // 2

