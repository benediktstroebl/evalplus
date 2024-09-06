def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting with 1 and
    # ending with 1, as well as starting with 1 and ending with 11, etc.
    counts = [0] * (n * 2 + 1)
    
    # Initialize the starting and ending values for the range of n-digit numbers.
    start, end = 1, 1
    
    # Loop through the range of n-digit numbers and update the count for
    # numbers that start or end with 1.
    while start <= end:
        mid = (start + end) // 2
        if mid * 10 + 1 <= end and mid * 10 + 1 + n <= end:
            counts[mid * 10 + 1] += 1
        if mid * 10 + 1 <= end and mid * 10 + 1 + n <= end:
            counts[mid * 10 + 1 + n] += 1
        
        if mid * 10 + 1 <= end:
            start = mid * 10 + 1
        else:
            end = mid * 10 + 1 + n
    
    # Return the total count of numbers that start or end with 1.
    return sums(counts)