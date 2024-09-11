```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to perform the circular shift on
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The result of the circular shift as a string
    """
    # Convert the number to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, in case shift > len(x_str)
    effective_shift = shift % len(x_str)
    
    # Perform the circular shift
    if effective_shift == 0:
        return x_str
    else:
        return x_str[-effective_shift:] + x_str[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift`, performs the circular shift, and returns the result as a string. The effective shift is calculated to handle cases where `shift > len(x_str)`, and the result is returned as a string. The test cases at the end demonstrate the function's behavior.