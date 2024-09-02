
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    # if n is 1 digit, the count of n-digit positive integers will be
    # the count of n-digit positive integers ending with 1 - (count of n-digit
    # positive integers starting with 1), and the count of n-digit positive
    # integers starting with 1 will be the count of n-digit positive integers
    # ending with 1 - (count of n-digit positive integers ending with 1
    n_1 = count_starts_one_ends(n - 1)
    n_0 = count_starts_one_ends(n) - n_1
    return n_1 + n_0
