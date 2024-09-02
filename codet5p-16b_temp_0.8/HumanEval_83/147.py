
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1: return 1
    elif n == 2: return 1 + 2
    elif n == 3: return 2 + 1
    else:
        return starts_one_ends(n-1) + ends_one_ends(n)
