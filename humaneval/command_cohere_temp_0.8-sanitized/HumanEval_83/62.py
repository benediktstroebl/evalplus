def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Initialize the count of numbers to 0
    count = 0
    # Calculate the count for numbers with  '1' at the beginning and end.
    for i in range(1, n + 1):
        count += (10 ** (n - i - 1) - 1) / 9
    # Calculate the count for numbers with '1' at the beginning or end.
    for i in range(1, n + 1):
        count += (10 ** (n - i - 1) - 1) / 9 + (10 ** i - 1) / 9
    return count