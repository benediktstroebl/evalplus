
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1111111111...
    if n > 10:
        return 0
    if n == 1:
        return 2

    # 1000000000...
    if n < 2:
        return 0

    # 11111111110
    return 2
