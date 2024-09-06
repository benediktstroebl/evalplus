def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 9)
    
    # Count the numbers that start with 1
    for i in range(1, n + 1):
        counts[i - 1] += 1
    
    # Correct the calculation for numbers that end with 1
    counts[n * 8 - 1:] = counts[n * 8 - 1:] - counts[:-1]
    
    return sum(counts)