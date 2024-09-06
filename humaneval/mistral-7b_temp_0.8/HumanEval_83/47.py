
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0

    start_one = 9 ** (n - 1)
    end_one = 9 ** (n - 1)
    return start_one + end_one

