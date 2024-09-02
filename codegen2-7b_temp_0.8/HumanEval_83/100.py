
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(map(lambda x: x[0] == 1 or x[-1] == 1, itertools.count(n)))
