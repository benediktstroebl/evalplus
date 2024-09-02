
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(
        (i + 1) * sum(i + 1 > 9 * n) for i in range(0, 9 * n, 10)
    )
