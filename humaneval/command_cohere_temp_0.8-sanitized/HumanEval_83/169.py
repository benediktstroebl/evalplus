def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This list will have (10 ** n) elements.
    counts = [0] * (10 ** n)
    
    # Count the numbers that start with 1
    for i in range(1, 10 ** (n - 1)):
        counts[i] += 1
    
    # Correct the counts to avoid double-counting
    counts[1] = 0
    
    # Count the numbers that end with 1
    for i in range(10 ** (n - 1), 0, -1):
        counts[i] += 1
    
    return sum(counts)