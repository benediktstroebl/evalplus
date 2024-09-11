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
        str: The result as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(str_x)
    # Split the string into two parts
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    # Return the two parts in reverse order
    return first_part + second_part

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift (in case `shift > number of digits`), splits the string into two parts, and returns the two parts in reverse order. The test cases at the end demonstrate the function's behavior with different inputs.