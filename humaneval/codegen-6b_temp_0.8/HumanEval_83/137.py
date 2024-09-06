
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 4
    elif n == 2:
        return 7
    elif n == 3:
        return 8
    return sum(starts_one_ends(i - 1) for i in range(n + 1, n + 4) if 1 == n * 10 ** (n - i))

