
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num = 0
    while n > 0:
        num += len(nums_between(n))
        n -= 9
    return num

