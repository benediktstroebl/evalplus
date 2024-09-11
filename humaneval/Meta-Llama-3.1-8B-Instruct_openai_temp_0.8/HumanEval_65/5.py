```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to circular shift
    shift (int): The number of positions to shift
    
    Returns:
    str: The result of the circular shift as a string
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    shift = shift % len(str_x)
    return str_x[-shift:] + str_x[:-shift]

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift(x, shift)` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift by taking the modulus of the shift with the length of the string (to handle cases where the shift is greater than the number of digits), and then returns the result of the circular shift by concatenating the shifted part with the unshifted part. The function is then tested with the provided examples.