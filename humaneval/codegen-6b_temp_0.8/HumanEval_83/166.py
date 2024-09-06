
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    from math import ceil, log10
    return len([x for x in xrange(1, 10**n) if ceil(log10(x)) == 1])

