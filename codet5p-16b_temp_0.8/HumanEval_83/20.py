
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 0:
        return 0
    else:
        count = 0
        for i in range(1, 10):
            count += starts_one_ends(n - 1)
        for i in range(1, 10):
            count += ends_one(n - 1)
        return count
