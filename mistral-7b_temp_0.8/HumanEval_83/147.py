
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ones = 0
    for i in range(n):
        ones += 1 + (n-1-i)*10**i
    return ones

