def starts_one_ends(n):
    # Create a list to store the results for base cases. 
    counts = [0 for i in range(n + 1)]

    # Count the numbers that start with 1. 
    counts[1] = 1

    # Count the numbers that end with 1. 
    counts[n] = 1

    # Iterate over from 2 to n-1, handle intermediate cases.
    for i in range(2, n):
        counts[i] = counts[i - 1] + counts[i + 1]
        
        # Subtract the numbers that start with 1 from the total counts. 
        counts[i] -= counts[i - 1]
        # Subtract the numbers that end with 1 from the total counts. 
        counts[i] -= counts[i + 1]
    
    return counts[n]