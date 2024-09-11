```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts: the part to be shifted to the end, and the rest
    shifted_part = num_str[-effective_shift:]
    rest = num_str[:-effective_shift]
    
    # Combine the two parts in the correct order
    result = shifted_part + rest
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input. It converts the integer to a string, calculates the effective shift amount, splits the string into two parts, and combines them in the correct order to produce the shifted result. The test cases at the end demonstrate the function's behavior.