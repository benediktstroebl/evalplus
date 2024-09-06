
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for x in range(10, n * 10 + 1, 10) if x.startswith('1') or x.endswith('1'))

