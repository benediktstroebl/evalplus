
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # counters for start and end with 1
    count_starts = 0
    count_ends = 0
    for i in range(n):
        count_starts += count_starts * 9 + 1
        count_ends += count_ends * 9 + 1
    return count_starts + count_ends - 2

