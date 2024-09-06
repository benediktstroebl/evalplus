def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1.
    count = [0] * (n + 1)
    # Initialize the count of numbers starting or ending with 1 to zero.
    count[1] = 0
    # For every number between 1 and n:
    for num in range(2, n + 1):
        # Increment the count of numbers starting or ending with 1 for this number.
        count[num] += 1
    return sum(count)