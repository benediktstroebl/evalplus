
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    one_starts = 0
    one_ends = 0
    for d in range(1, n + 1):
        one_starts += 9 * ncr(d - 1, 8)
        one_ends += 9 * ncr(d - 1, 7)
    return one_starts + one_ends
