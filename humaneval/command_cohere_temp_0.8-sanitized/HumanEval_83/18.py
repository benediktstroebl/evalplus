def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the count of numbers that start or end with 1.
    count = [0] * (n + 1)
    # Initialize the count of numbers that start or end with 1 for 1-digit numbers.
    count[1] = 1
    # Calculate the count of numbers that start or end with 1 for 2 to n-digit numbers.
    for i in range(2, n + 1):
        count[i] = count[i - 1] + count[i] + count[i + 1]
    # Return the count of numbers that start or end with 1.
    return count[n]