
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    l = n - 1
    if n == 1:
        return 0
    else:
        return int(l * 9 ** (n - 1) + l * 10 ** (n - 2)) + int(10 ** (n - 1))

