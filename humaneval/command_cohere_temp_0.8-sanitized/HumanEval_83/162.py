def starts_one_ends(n):
    # Create a list to store the results for 
    # each number of digits from 1 to n
    result = [0] * (n + 1)
    
    # For 1 to n digits, check if the last digit is 1
    for digits in range(1, n + 1):
        # Check if the last digit is 1
        result[digits] += 9 * (n - digits) // 10
    
    # If the number starts with 1, it is counted in the 
    # respective digit bucket, so it is excluded here
    return sum(result) - result[1]