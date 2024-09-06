
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n > 0:
        n = n - 1
        count = (n // 10) + ((n % 10 == 1) + (n % 10 == 9))
    return count
