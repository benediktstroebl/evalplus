
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 2**0 = 1, 2**1 = 1, 2**2 = 2, 2**3 = 1, 2**4 = 8, 2**5 = 32, ...
    return sum(2**digit for digit in range(n - 1, -1, -1))
