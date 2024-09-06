
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return 2 * len([d for d in map(int, list(str(n))) if d == 1])

