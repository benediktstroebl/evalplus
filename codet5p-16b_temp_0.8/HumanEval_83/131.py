
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1

    start = 1
    ends = 0

    for i in range(1, n):
        start += 10**(i - 1) * (i)
        ends += (10**i - 10**(i - 1))

    return start + ends + 1

