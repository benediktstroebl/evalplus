def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1.
    count = [0] * (n + 1)
    # Initialize the count of numbers starting or ending with 1 for 1-digit numbers.
    count[1] = 1
    if n >= 2:
        # Calculate the counts for numbers starting or ending with 1 for 2 and more digits.
        count[2] = count[1]
        for i in range(3, n + 1):
            count[i] = count[i - 1] + count[i - 2]
    return count[n]