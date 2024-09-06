
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    for i in range(1, n+1):
        if i % 10 == 1:
            yield i
        elif i % 10 == 0:
            yield i

