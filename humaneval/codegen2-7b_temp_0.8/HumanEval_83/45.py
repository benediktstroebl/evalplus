
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(i for i in range(10, n+1) if is_10_one_start(i) or is_10_one_end(i
