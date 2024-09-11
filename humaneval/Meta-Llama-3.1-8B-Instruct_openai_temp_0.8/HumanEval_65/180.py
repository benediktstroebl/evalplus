```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted string.
    """
    # Convert the integer to a string to be able to shift the digits
    x_str = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Shift the digits right by the effective shift and return the result
    return x_str[-effective_shift:] + x_str[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift amount `shift`. It converts the integer to a string, calculates the effective shift in case it exceeds the number of digits, and then returns the shifted string. The test cases at the end demonstrate the function's behavior.