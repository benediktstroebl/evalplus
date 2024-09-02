
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_digits = len(str(n))
    return (n_digits * n) + 1
