
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    starts_with_1 = starts_one_ends_helper(n, n)
    starts_with_1 += starts_one_ends_helper(n, n-1)
    starts_with_1 += starts_one_ends_helper(n-1, n)
    return starts_with_1
