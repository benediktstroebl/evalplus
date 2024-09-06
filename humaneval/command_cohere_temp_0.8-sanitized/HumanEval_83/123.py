def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers without considering the starting or ending digit, then subtracts
    # the numbers that do not start or end with 1.
    counts = [((10 ** (i - 1)) * 10) - 9 for i in range(1, n + 1)]
    
    # Loop through the possible counts for n-digit numbers and adjust
    # the count for starting or ending with 1 for each n-digit number.
    for i in range(1, n + 1):
        counts[i - 1] += 9 * (n - i) // 2  
    
    return counts[n - 1]