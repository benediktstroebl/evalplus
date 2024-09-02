
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    starts = ends = 0
    for i in range(1, n):
        starts += 10**i - 9*10**(i-1)
        ends += 10**i - 9*10**(i-1) + 1
    return starts + ends
