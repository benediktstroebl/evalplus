def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 9)
    
    # Amount of numbers starting with 1 and of length n
    for i in range(1, n + 1):
        counts[i - 1] = counts[i] + 1
    
    # Amount of numbers ending with 1 and of length n
    for i in range(n, 0, -1):
        counts[i] = counts[i - 1] + 1
    
    # Return the total count of numbers that start or end with 1
    return sums(counts)