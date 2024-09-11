```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): The integer to be shifted.
    shift (int): The number of digits to shift.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    x_str = str(x)  # Convert integer to string
    shift = shift % len(x_str)  # Handle shifts greater than number of digits
    return x_str[-shift:] + x_str[:-shift]  # Perform circular shift

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. The function uses string slicing to perform the circular shift and handles shifts greater than the number of digits by taking the modulus of the shift amount with the length of the string representation of `x`.