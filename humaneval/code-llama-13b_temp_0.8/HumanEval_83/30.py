
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count the number of n-digit numbers that start with 1.
    count = 1 if n <= 1 else 0

    # Count the number of n-digit numbers that end with 1.
    count += 1 if n <= 1 else 0

    return count

