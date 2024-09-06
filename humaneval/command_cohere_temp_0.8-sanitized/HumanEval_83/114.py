def starts_one_ends(n):
    # Create a list to store the results for bases from 1 to n
    result = [0] * (n + 1)
    
    # Base 1: All numbers end with 1
    result[1] = 1
    
    # Base 2 and beyond: Count numbers that start or end with 1
    for base in range(2, n + 1):
        result[base] += int(base == 1 or base % 2 == 0)
    
    return sum(result)