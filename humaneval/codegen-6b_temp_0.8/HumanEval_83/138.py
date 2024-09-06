
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 6
    else:
        return starts_one_ends(n-1) + 10*starts_one_ends(n-2) + 8*starts_one_ends(n-3)
