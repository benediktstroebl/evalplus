
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # we count all numbers that start with 1 and are n-1 long,
    # and all numbers that end with 1 and are n-1 long.
    return 10**(n-1) * (2 if n > 1 else 1)
