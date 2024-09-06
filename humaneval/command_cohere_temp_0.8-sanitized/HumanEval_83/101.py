def starts_one_ends(n):
    # Create a list to store the results for 
    # different lengths of n
    counts = [0] * (n + 1)
    
    # For each length, determine the number of
    # numbers that start or end with 1
    for i in range(1, n + 1):
        counts[i] += 2 * 10 ** (n - i)
    
    return counts[n]