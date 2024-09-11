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
        str: The shifted integer as a string.
    """
    x_str = str(x)
    shift = shift % len(x_str)
    return x_str[-shift:] + x_str[:-shift]


# Test the function
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input. It converts the integer to a string, calculates the effective shift (which is the remainder of shift divided by the number of digits, to handle cases where shift is greater than the number of digits), and then returns the shifted string by concatenating the last `shift` characters with the rest of the string.