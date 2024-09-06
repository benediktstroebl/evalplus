def starts_one_ends(n):
    # Create a list to store the digits
    num_digits = list(range(1, n + 1))
    
    # Handle the edge case for n = 1
    if n == 1:
        return 2
    
    # Consider starting with 1
    count_start = 1
    for i in range(n - 1):
        count_start *= 9
        count_start += num_digits[i]
    
    # Consider ending with 1
    count_end = 1
    for i in range(n - 1, 0, -1):
        count_end *= 9
        count_end += num_digits[i]
    
    return count_start + count_end