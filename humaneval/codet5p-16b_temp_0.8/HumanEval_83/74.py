
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    one_ends = 0
    for i in range(1, 10 ** n):
        if i % 10 == 1 or i % 10 == 0:
            one_ends += 1
    return one_ends
