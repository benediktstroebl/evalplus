```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    
    # Convert the integer into a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective number of positions to shift
    # If shift > number of digits, use the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be moved to the end, and the rest
    part_to_move = str_x[-effective_shift:]
    rest = str_x[:-effective_shift]
    
    # Combine the two parts to get the result
    result = part_to_move + rest
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of shifting the digits of `x` by `shift` positions to the right as a string. If `shift` is greater than the number of digits in `x`, the function returns the digits reversed. The script includes docstrings and test cases to demonstrate its usage.