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

    # Convert the integer to a string to easily access its digits
    str_x = str(x)

    # Calculate the effective shift, handle cases where shift > number of digits
    effective_shift = shift % len(str_x)

    # If shift > number of digits, equivalent to shifting by (number of digits - shift) places
    if effective_shift == 0:
        effective_shift = len(str_x)

    # Perform the circular shift by slicing the string
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]

    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, shifts the digits of `x` to the right by `shift` places, and returns the result as a string. The function handles cases where `shift` is greater than the number of digits in `x` by using the modulo operator to calculate the effective shift. The script also includes test cases to demonstrate the function's behavior.