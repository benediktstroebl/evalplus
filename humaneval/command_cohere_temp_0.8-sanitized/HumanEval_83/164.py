def starts_one_ends(n):
    # Create a list to store the results for  1st and last position
    counts = [0 for i in range(n+1)]
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Calculate counts of numbers that end with 1
    for i in range(2, n+1):
        counts[i] += counts[i-1]
    
    return counts[-1]