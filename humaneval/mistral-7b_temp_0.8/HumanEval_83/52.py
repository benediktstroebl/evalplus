
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1 + 1 + 2 + 2 + ... + 9 + 9 + 10 = 45
    return 9 * n + 45

