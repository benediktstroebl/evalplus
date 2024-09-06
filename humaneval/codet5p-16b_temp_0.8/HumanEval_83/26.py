
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def starts_one_ends_helper(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return starts_one_ends_helper(n-1) + starts_one_ends_helper(n-2)
    return starts_one_ends_helper(n)
