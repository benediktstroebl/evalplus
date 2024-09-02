
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    starts_one_ends_count = 0

    if n == 1:
        starts_one_ends_count += 1
    else:
        for _ in range(1, 10 ** n - 1):
            if _ % (10 ** (n - 1)) == 1 or _ % (10 ** (n - 1)) == 10 ** (n - 1) - 1:
                starts_one_ends_count += 1

    return starts_one_ends_count

