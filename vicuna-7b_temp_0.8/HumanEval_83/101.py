
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n < 10:
        return n
    return n * (n // 10) * (n // 100) + (n // 10)
