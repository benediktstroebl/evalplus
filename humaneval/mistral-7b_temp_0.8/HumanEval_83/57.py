
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_starts = 0
    num_ends = 0

    for i in range(n):
        num_starts += pow(10, i)
        num_ends += (pow(10, n) - pow(10, i))
    return num_starts + num_ends


