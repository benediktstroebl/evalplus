def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number with no leading zeros, where n >= 1
    counts = [0] * ((n + 1) * 10 - 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    counts[10 ** (n - 1)] = 1
    
    # Sum the counts of numbers that start or end with 1
    return sum(counts)