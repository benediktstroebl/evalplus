def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes singles digits,
    # doubles digits, and so on up to n-digit numbers.
    counts = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    
    # Initialize the left-most column as zeros (for numbers that are less than 10)
    for i in range(10, n + 1):
        counts.insert(0, 0)
    
    # Increment counts for numbers starting or ending with 1.
    for i in range(1, 10):
        counts[i] += 1
        counts[i] += counts[i-1]
    
    return counts[-1]