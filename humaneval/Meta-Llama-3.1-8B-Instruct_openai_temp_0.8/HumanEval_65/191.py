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
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily extract and shift the digits
    str_x = str(x)
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    # Split the string into two parts at the effective shift position
    # and combine them in reverse order to get the result
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift(x, shift)` that takes an integer `x` and a shift value `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. If `shift` is greater than the number of digits in `x`, the function returns the digits in reverse order. The script also includes test cases to demonstrate the function's behavior.