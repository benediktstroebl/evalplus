def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Count numbers that start with 1
    start_with_one = 1 if n >= 1 else 0
    
    # Count numbers that end with 1
    if n >= 1:
        ends_with_one = digits[0] if digits[0] == 1 else 0
    else:
        ends_with_one = 0
    
    # Return the total count
    return start_with_one + ends_with_one