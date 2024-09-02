
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    elif n < 3:
        return 1
    else:
        return (1 << (n-1)) + (1 << (n-1))
