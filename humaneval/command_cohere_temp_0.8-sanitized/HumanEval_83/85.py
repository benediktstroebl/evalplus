def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a count array to store the counts of numbers starting or ending with 1.
    counts = [0] * (n + 1)
    # Initialize the count of numbers starting or ending with 1 to 1.
    counts[1] = 1
    # Count the numbers starting or ending with 1 for numbers from 2 to n*n.
    for num in range(2, n * n + 1):
        if (num % 10) == 1:
            counts[num] += 1
    # Return the final count of numbers starting or ending with 1.
    return sums(counts)