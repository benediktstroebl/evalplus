def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a variable to store the count of numbers.
    count = 0
    # Iterate through each digit position from the second to the nth position.
    for i in range(1, n+1):
        # For each position, consider both starting and ending with 1.
        count += 2 * 10 ** (n - i - 1)
    return count