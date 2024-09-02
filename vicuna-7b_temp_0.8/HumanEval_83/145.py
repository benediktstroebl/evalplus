
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n-digit numbers that end with 1
    end_ones = sum(1 for i in range(n) if n % i == 0)
    # n-digit numbers that start with 1
    start_ones = sum(1 for i in range(n) if n // i == 1)
    # return the sum of end and start ones
    return end_ones + start_ones
