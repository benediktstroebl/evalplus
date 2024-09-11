```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the number to a string to easily access and manipulate its digits
    num_str = str(x)
    # Calculate the effective shift, considering the possibility of shift > number of digits
    effective_shift = shift % len(num_str)
    # Split the string into two parts at the shift position from the end
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    # Return the shifted string by concatenating the two parts in reverse order
    return first_part + second_part

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script uses the modulo operator (`%`) to calculate the effective shift, taking into account the possibility of shift being greater than the number of digits. The string is then split into two parts at the shift position from the end, and these two parts are concatenated in reverse order to form the shifted string.