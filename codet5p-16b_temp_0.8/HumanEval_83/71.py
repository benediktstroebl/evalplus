
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2

    starts_with_1 = ends_with_1 = 0
    for i in range(1, n):
        starts_with_1 += starts_one_ends(i)
        ends_with_1 += starts_one_ends(n - i)

    return starts_with_1 + ends_with_1

