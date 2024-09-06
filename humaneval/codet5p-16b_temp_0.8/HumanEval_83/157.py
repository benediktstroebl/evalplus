
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    num_starts_ends = 0

    for i in range(10**n):
        if (i % (10**(n-1)) == 0) or (i % (10**(n-1)) == 1):
            num_starts_ends += 1

    return num_starts_ends

