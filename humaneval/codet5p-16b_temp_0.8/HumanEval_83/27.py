
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert n > 0

    starts_with_1 = 0
    starts_with_1 += ends_with(n - 1, n - 1)[0]
    starts_with_1 += ends_with(n - 2, n - 2)[0]
    starts_with_1 += ends_with(n - 3, n - 3)[0]

    ends_with_1 = 0
    ends_with_1 += starts_with(n - 1, n - 1)[1]
    ends_with_1 += starts_with(n - 2, n - 2)[1]
    ends_with_1 += starts_with(n - 3, n - 3)[1]

    return starts_with_1, ends_with_1

