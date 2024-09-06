def starts_one_ends(n):
    # Create a list to store the results for bases from 1 to n
    result = [0] * (n + 1)
    
    # Count the numbers that start with 1
    result[1] = 1
    
    # Count the numbers that end with 1
    half_n = n // 2
    for base in range(2, half_n + 1):
        result[base] += result[base - 1]
    
    # Adjust the count for numbers that start and end with 1
    result[1] -= result[0]
    result[n] -= result[n - 1]
    
    return result[n]