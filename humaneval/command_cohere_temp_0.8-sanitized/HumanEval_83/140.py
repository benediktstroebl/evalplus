def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers, without considering the starting or ending digit, then subtracts
    # the numbers that do not start or end with 1.
    counts = [n * (n + 1) // 2 - n // 2 for n in range(1, n + 1)]
    
    # Return the maximum count, which occurs when n is 9 or 10
    return max(counts)