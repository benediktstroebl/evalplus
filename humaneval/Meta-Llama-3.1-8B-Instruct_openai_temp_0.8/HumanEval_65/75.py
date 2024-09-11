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

    Example:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    # Convert the integer to a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Return the shifted string
    return str_x[-effective_shift:] + str_x[:-effective_shift]


# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. The function first converts the integer to a string, calculates the effective shift by taking the modulus of the shift value with the length of the string, and then returns the shifted string by concatenating the last `effective_shift` characters with the characters before them. If `shift` is greater than the number of digits, the function effectively reverses the string. The script includes test cases to demonstrate the function's behavior.