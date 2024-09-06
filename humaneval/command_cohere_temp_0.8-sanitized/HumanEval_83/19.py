def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the case where n = 1
    if n == 1:
        return 2
    
    # Handle the case where n is even (the number starts with 1 and ends with 1)
    if n % 2 == 0:
        return digits[0]
    
    # Subtract cases where the number ends with 1 (not considering the starting 1)
    return digits[0] - digits[n // 2] + 1