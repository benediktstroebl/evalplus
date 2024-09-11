```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily extract and shift its digits
    str_x = str(x)
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(str_x)
    # Shift the digits to the right by slicing the string
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. The effective shift is calculated by taking the remainder of `shift` divided by the number of digits in `x`, to handle cases where `shift` is greater than the number of digits. The digits are then shifted to the right by slicing the string representation of `x` and concatenating the last `effective_shift` characters with the rest of the string. The script also includes test cases to verify the correctness of the `circular_shift` function.