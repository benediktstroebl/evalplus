
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count all multiples of 10 (including 1 & 10)
    # Each of these multiples of 10 starts with 1
    # Each of these multiples of 10 ends with 1
    # -1 because we don't count the last digit
    return (n // 10 + 1) * 2 - 1

