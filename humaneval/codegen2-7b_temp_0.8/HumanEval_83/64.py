
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ones = 0
    for i in range(1, int(n/10) + 1):
        ones += n%10 == 1
    return ones
