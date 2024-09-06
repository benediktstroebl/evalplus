def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 10
    max_num = 10**n - 10
    min_num = 10**(n-1) + 1
    return max_num - min_num