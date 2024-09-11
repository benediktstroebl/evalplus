```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.
    
    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Perform the circular shift
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input. It first converts the integer to a string, then calculates the effective shift by taking the remainder of `shift` divided by the number of digits in the string. The function then performs the circular shift by slicing the string and concatenating the last `effective_shift` characters with the rest of the string. Finally, the function returns the shifted string.