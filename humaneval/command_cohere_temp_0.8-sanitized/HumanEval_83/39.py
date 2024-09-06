def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Remove the starting and ending 1 if present
    if digits[0] == 1:
        digits.pop(0)
    if digits[-1] == 1:
        digits.pop(-1)
    
    # Count the remaining digits
    count = len(digits)
    
    return count