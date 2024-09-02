
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2

    if n == 2:
        return 3

    # by induction hypothesis
    num = 3

    # count numbers ending in 1
    for i in range(2, n):
        num += 9 * 10 ** (i - 1)

    # count numbers starting in 1
    num += 10 ** (n - 1)

    return num
