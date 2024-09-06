def starts_one_ends(n):
    # Create a list to store the counts for starting and ending with 1
    counts = [0, 0]
    
    # Loop through numbers from 1 to n*10
    for num in range(1, (n * 10) + 1):
        # Increment counts[0] if the number starts with 1
        if num % 10 == 1:
            counts[0] += 1
        # Increment counts[1] if the number ends with 1
        if num >= 10 and num % 10 == 1:
            counts[1] += 1
    
    # Return the sum of the counts
    return counts[0] + counts[1]