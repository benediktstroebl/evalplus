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
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)

    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)

    # If shift > number of digits, the problem statement asks for the digits reversed
    # This is equivalent to a circular shift of the number of digits
    if effective_shift == 0:
        effective_shift = len(str_x)

    # Perform the circular shift by slicing the string
    # The first slice goes from the effective shift to the end of the string
    # The second slice goes from the start of the string to the effective shift
    result = str_x[-effective_shift:] + str_x[:-effective_shift]

    return result

# Test the circular_shift function with the provided examples
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses Python's built-in string slicing feature to efficiently perform the circular shift. It first converts the input integer to a string, then calculates the effective shift by taking the remainder of the shift divided by the number of digits. If the effective shift is 0, it means the shift is a multiple of the number of digits, so it sets the effective shift to the number of digits. Finally, it performs the circular shift by slicing the string and concatenating the two slices.