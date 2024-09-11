```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily slice and join the digits
    str_x = str(x)
    
    # Calculate the effective shift, considering that shift > number of digits
    # is equivalent to shift % number of digits
    effective_shift = shift % len(str_x)
    
    # If shift is zero or len(str_x), the string is not changed
    if effective_shift == 0 or effective_shift == len(str_x):
        return str_x
    
    # Split the string into two parts at the shift point and concatenate them
    # in reverse order to get the shifted string
    left_part = str_x[:-effective_shift]
    right_part = str_x[-effective_shift:]
    shifted_str = right_part + left_part
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(1234, 1))  # "4321"
print(circular_shift(1234, 5))  # "1234"
```