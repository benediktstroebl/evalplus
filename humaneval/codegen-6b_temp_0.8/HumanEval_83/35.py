
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return len([str(n) for n in xrange(10**n) if n >= 1 and str(n).startswith('1') or str(n).endswith('1')])
