
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    #starts_one_ends = 0
    if n < 1:
        return starts_one_ends
    else:
        start_one = 9*(n-1) + 1
        ends_one = 9*n
        starts_one_ends = ends_one - start_one + 1
        return starts_one_ends
