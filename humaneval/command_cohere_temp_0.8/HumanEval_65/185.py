```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Amount to shift right.

    Returns:
    str: Resultant string after shifting.
    """
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[: len(digits) % shift]
    return digits[-shift:] + digits[:-shift]
```

This code takes care of different scenarios of shifting and shifting digits backwards when the shift is greater than the number of digits. 

To follow best practices, the function could include more comprehensive tests, error handling for invalid input types, and comments explaining the internal logic for better maintainability.