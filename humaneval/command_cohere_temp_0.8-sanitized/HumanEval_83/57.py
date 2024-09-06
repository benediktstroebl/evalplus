def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a 2D list to store the counts of numbers starting and ending with 1.
    # The dimensions of the 2D list are (n + 1) x 2, bounded by (10, 2) to handle edge cases.
    counts = [[[0 for _ in range(2)] for _ in range(n + 1)] for _ in range(10)]
    # Initialize counts for 1-digit numbers.
    for i in range(1, 10):
        counts[i][0] = 1 if i % 10 == 1 else 0
    # Iterate through 2-digit numbers and update the counts.
    for i in range(1, 10):
        for j in range(1, 10):
            if i * 10 + j <= 99:
                counts[i][0] += 1
                counts[i][1] += 1
                counts[i][0] += 1 if (i * 10 + j) % 10 == 1 else 0
                counts[i][1] += 1 if (i * 10 + j) % 10 == 1 else 0
    # Use nested list comprehensions to calculate the counts for n-digit numbers.
    return [[sum(counts[i][j] for i in range(10)) for j in range(2)] for _ in range(n)]