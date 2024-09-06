
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # The number of positive integers n-digit is 10^n
    count = 10**(n-1)

    # Count of numbers starting with 1.
    count += 9**(n-1)

    # Count of numbers ending with 1.
    count += 9**(n-1)

    return count
