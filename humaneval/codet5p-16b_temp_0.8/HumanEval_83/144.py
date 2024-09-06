
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 10

    count = 0

    if n >= 2:
        count += starts_one_ends(n-1)

    for i in range(1, 10):
        if n >= 2 and i % 10 == 1:
            count += starts_one_ends(n-2)

        if n >= 2 and i == 1:
            count += starts_one_ends(n-2)

    return count

