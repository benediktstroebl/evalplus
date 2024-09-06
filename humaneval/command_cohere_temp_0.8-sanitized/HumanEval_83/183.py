def starts_one_ends(n):
    # Create a list to store the count of numbers
    count = [0] * (n + 1)
    
    # Count the numbers that start with 1
    count[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        count[i] += count[i - 1]
    
    return count[n]