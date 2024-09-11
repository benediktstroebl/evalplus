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
        str: The shifted integer as a string.

    Example:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # and concatenate them in reverse order
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It shifts the digits of `x` to the right by `shift` positions and returns the result as a string. The script also includes example usage and a docstring to explain the function's behavior.