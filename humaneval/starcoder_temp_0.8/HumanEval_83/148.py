
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1

    start_ones = 9
    end_ones = 9

    for _ in range(2, n):
        start_ones *= 10 - 1
        end_ones *= 10 - 1

    return start_ones + end_ones
