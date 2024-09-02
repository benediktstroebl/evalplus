
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    else:
        return (sum(1 for _ in range(n // 2)) +
               sum(1 for _ in range(n // 2, n // 2 - 1, 2)))
