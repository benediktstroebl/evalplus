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
    num_str = str(x)  # Convert the integer to a string
    shift = shift % len(num_str)  # In case shift > number of digits
    return num_str[-shift:] + num_str[:-shift]  # Perform the circular shift


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script uses string slicing to perform the circular shift. The `[-shift:]` slice takes the last `shift` characters of the string, and the `[:-shift]` slice takes all characters except the last `shift` characters. By concatenating these two slices, we get the result of the circular shift. The `shift % len(num_str)` expression ensures that the shift is within the bounds of the number of digits in the string.