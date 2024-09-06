def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers without considering the start or end value.
    num_counts = [0] * (n * 9 + 1)
    for i in range(1, n + 1):
        # For each possible length n down to 1 digit, count the number of
        # permutations that fit the n-digit criteria.
        for j in range(1, 10):
            num_counts[i * 10 - 1] += 1

    # Count numbers that start with 1 and remove counts that overlap with
    # numbers that end with 1, since they are counted twice.
    return num_counts[1] - num_counts[10]