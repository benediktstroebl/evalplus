def starts_one_ends(n):
    # Create a list to store the results for 	values of n from 1 to n.
    counts = [0] * (n + 1)
    
    for num in range(1, n + 1):
        # Calculate the numbers of n-digit positive integers that start with 1.
        counts[num] += 1
        
        # Remove the starting 1 to get the numbers of n-digit positive integers that end with 1.
        counts[num] += counts[num - 1]
    
    return counts[-1]