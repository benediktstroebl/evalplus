
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    end1 = sum([1**i for i in range(1, n)])
    starts1 = sum([1**i for i in range(1, n)])
    return end1 + starts1

