
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ones = 0
    for i in range(10):
        ones += int(str(i) + '1' * (n - 1))
        ones += int('1' * (n - 1) + str(i))
    return ones
