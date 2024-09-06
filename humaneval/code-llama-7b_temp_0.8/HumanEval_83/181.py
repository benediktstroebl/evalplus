
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n1_count = 0
    if n >= 1:
        n1_count = 2
    if n >= 2:
        n1_count += 8 * 9 ** (n - 2)
    if n >= 3:
        n1_count += 2 * 9 ** (n - 3)
    return n1_count

