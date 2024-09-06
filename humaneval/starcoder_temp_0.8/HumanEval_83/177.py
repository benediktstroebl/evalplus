
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(x for x in range(1, 10**n) if x.startswith('1') or x.endswith('1'))
