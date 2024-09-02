
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    # First case is 101...n1, and the last digit must be 1.
    count += n

    # Second case is 100...n01, and the last digit must be 0.
    count += n - 1

    return count
