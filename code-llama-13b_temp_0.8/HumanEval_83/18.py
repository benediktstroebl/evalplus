
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # depending on the meaning of the problem, this test may need to be
    # changed
    if n < 1:
        return 0

    # the number of n-digit numbers that start with 1 is equal to the number of
    # n-digit numbers that end with 1
    return 10**(n-1)

