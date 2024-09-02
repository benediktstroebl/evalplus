
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count of numbers that start with 1
    num_ones = 0
    for i in range(2, n+1):
        if i == 1 or i % 10 == 1:
            num_ones += 1
    return num_ones
