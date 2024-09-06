def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number.
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    for i in range(1, n + 1):
        counts[i] += 1
    
    # Count the numbers that end with 1
    for i in range(n, 0, -1):
        counts[i] += 1
    
    return sums(counts)
n = 5