
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_ones = 0
    for i in range(10):
        num_ones += i * factorial(9 - i) * n * (n - 1) * (n - 2) // 6

    return num_ones

