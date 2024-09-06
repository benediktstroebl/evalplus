
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert n > 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    cnt = 0

    for i in range(1, 10 ** (n - 1)):
        cnt += starts_one_ends(n - 1)

    for i in range(1, 10 ** (n - 1)):
        cnt += ends_one(n - 1)

    return cnt

