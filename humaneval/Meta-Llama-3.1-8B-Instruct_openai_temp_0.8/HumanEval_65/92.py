```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The result of the circular shift as a string
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the actual shift, taking into account if shift > number of digits
    actual_shift = shift % len(x_str)
    
    # Shift the digits to the right using string slicing
    shifted_str = x_str[-actual_shift:] + x_str[:-actual_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift(x, shift)` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string to easily manipulate the digits, calculates the actual shift, shifts the digits to the right using string slicing, and returns the result as a string. The function handles the case where `shift > number of digits` by taking the modulus of `shift` with the length of the string, effectively wrapping the shift around to the correct position.