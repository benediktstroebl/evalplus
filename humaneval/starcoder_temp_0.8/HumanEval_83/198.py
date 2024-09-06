
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(is_one_start(i) or is_one_end(i) for i in range(1, n + 1))

