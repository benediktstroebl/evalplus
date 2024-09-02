
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ones = 0
    tens = 0
    if n < 2:
        return 0
    elif n == 2:
        ones = 9
        tens = 9
    else:
        ones = (10 ** (n - 2) - 1) + (10 ** (n - 1) - 1)
        tens = (10 ** (n - 1) - 1) + (10 ** (n - 2) - 1)
    return ones + tens

