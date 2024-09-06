
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digits = len(str(n))

    return (10**digits) * (2 * 10**(digits - 1))
