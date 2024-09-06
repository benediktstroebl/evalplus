
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 10
    elif n == 2:
        return 22
    elif n == 3:
        return 100

    return starts_one_ends(n - 1) + ends_one_starts(n - 1)
