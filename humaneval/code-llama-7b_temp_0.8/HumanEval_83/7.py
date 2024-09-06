
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 10
    elif n == 1:
        return 8
    elif n > 1:
        return 8*starts_one_ends(n-1)
    else:
        return 0

