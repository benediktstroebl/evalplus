def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a variable to store the count of numbers that start or end with 1.
    count = 0
    # Count the numbers that start with 1
    if n >= 1:
        count += 9 ** (n - 1)
    # Count the numbers that end with 1
    if n >= 2:
        count += 9 ** (n - 2)
    return count