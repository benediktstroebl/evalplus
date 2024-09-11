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
    """
    x_str = str(x)
    shift = shift % len(x_str)  # In case shift is greater than number of digits
    return x_str[-shift:] + x_str[:-shift]

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, and returns the result of the circular shift as a string. The function works by converting the integer to a string, shifting the characters in the string by the specified amount, and then returning the result. The shift value is taken modulo the length of the string to handle cases where the shift value is greater than the number of digits.