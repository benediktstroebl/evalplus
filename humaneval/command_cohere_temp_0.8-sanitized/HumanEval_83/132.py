def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes the starting digits,
    # so the largest number considered is 99999...99 (10^n - 1).
    counts = [0] * ((10 * n) - 1)

    # Count the numbers that start with 1
    for i in range(1, ((10 * n) - 1) // 10):
        counts[i] += 1

    # Count the numbers that end with 1
    for i in range((10 * n) - 1, 0, -10):
        counts[i] += 1

    # Return the total count
    return sums(counts)