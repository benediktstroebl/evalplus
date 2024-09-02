
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    a1 = n - 1
    b1 = n
    a2 = n - 1
    b2 = n - 2
    return (a1 * b1) + (a2 * b2)
