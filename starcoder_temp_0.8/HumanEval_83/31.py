
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(1, n + 1):
        j = 10 ** (i - 1)
        k = 10 ** i - 1
        total += k - j + 1
    return total
