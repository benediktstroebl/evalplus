def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Count numbers that start with 1
    counts[0] = 1

    # Count numbers that end with 1
    for i in range(1, n):
        counts[i] = counts[i - 1] + 1

    return counts[-1]