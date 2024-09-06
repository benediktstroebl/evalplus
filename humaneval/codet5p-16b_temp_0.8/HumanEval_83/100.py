
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start_ends = [0] * (n + 1)
    start_ends[1] = 1
    start_ends[2] = 2
    for i in range(3, n + 1):
        start_ends[i] = start_ends[i - 1] + start_ends[i - 2]
    return start_ends[n]
