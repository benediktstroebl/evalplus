
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return int(str(n) + str(n)[1:]) if n > 0 else 0
