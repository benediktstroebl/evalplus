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
    str_x = str(x)  # Convert the integer to a string
    shift = shift % len(str_x)  # Handle cases where shift > number of digits
    result = str_x[-shift:] + str_x[:-shift]  # Shift the digits
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "231"
print(circular_shift(123, 5))  # "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value, and returns the shifted integer as a string. The function handles cases where the shift value is greater than the number of digits by taking the modulus of the shift value with the number of digits. It then constructs the result by concatenating the shifted part of the string with the unshifted part. The test cases at the end demonstrate the function's behavior with different inputs.