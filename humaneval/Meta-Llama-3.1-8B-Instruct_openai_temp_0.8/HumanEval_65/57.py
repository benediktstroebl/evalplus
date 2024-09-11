```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to be shifted.
        shift (int): The number of digits to shift.

    Returns:
        str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account cases where shift > len(x_str)
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be moved to the end, and the rest
    part_to_move = x_str[-effective_shift:]
    rest = x_str[:-effective_shift]
    
    # Combine the two parts in the correct order
    result = part_to_move + rest
    
    return result

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It uses the modulo operator to ensure the shift value is within the range of the number of digits in `x`. The function then splits `x` into two parts, one to be moved to the end and the rest, and combines them in the correct order to produce the result. The script includes test cases to verify the function's correctness.