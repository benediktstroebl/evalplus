
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_ends = sum(1 for d in range(1, n + 1) if (str(d) + str(d))[-1] == '1')
    one_starts = sum(1 for d in range(1, n + 1) if (str(d) + str(d))[0] == '1')
    return one_ends + one_starts
