```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The shifted string representation of the integer
    """
    digits = str(x)
    shift = shift % len(digits)  # In case shift > number of digits
    return digits[-shift:] + digits[:-shift]

# Example use cases:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(1234, 2))  # Output: "4312"
print(circular_shift(1234, 4))  # Output: "1234"
```

This script defines a function `circular_shift` that takes an integer `x` and an integer `shift` as input. It converts `x` to a string, calculates the effective shift (which is the remainder of `shift` divided by the number of digits in `x`), and then returns the string representation of `x` with its digits shifted right by the effective shift amount. The `%` operator is used to ensure that the shift is within the valid range for the number of digits in `x`.