
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def starts_one_ends_helper(n, num_ones):
        if n == 1:
            return 2
        if n == 2:
            return 9 * num_ones + 1
        return 10 * starts_one_ends_helper(n-1, num_ones + 1)
    return starts_one_ends_helper(n, 1)

