```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to perform the circular shift on.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    str_x = str(x)  # Convert the integer to a string
    num_digits = len(str_x)  # Get the number of digits in the string

    # Shift the digits
    shifted_str = str_x[-shift % num_digits:] + str_x[:-shift % num_digits]

    return shifted_str


# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script uses the modulus operator to handle cases where the shift is greater than the number of digits. The circular shift is achieved by slicing the string from the end of the string to the shift offset, then from the beginning of the string to the shift offset. The two slices are concatenated to form the shifted string.