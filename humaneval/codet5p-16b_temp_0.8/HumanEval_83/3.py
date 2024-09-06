
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    start_ones = end_ones = 0
    for i in range(1, n+1):
        if str(i)[0] == "1":
            start_ones += 1
        if str(i)[-1] == "1":
            end_ones += 1
    return start_ones + end_ones

