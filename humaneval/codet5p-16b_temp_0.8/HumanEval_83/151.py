
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2
    elif n == 2:
        return 6
    else:
        return starts_one_ends(n-1) + 2 + starts_one_ends(n-2)

