
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 10
    result = 0
    num = 1
    for i in range(n - 1):
        num *= 10
    one = num
    ten = 1
    for i in range(n - 2):
        ten *= 10
    for i in range(1, 10):
        result += one
        result += ten
        ten //= 10
        one *= 10
        one //= 10
    result += 10  # num //= 10
    return result
