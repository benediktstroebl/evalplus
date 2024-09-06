
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Must be 10 or more for either 1 or 0 to be in the middle
    if n < 10:
        return 0
    # all numbers that start with 1 have 10 digits
    # all numbers that end with 1 have 9 digits
    return (10 ** n - 10) // 9
