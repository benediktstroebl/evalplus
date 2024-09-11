```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits

    Returns:
        str: The result of the circular shift as a string
    """
    # Convert the integer to a string
    str_x = str(x)

    # Calculate the effective shift, taking into account if shift > len(str_x)
    effective_shift = shift % len(str_x)

    # Perform the circular shift
    result = str_x[-effective_shift:] + str_x[:-effective_shift]

    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script uses Python's string slicing feature to perform the circular shift. The `effective_shift` is calculated by taking the modulus of `shift` with the length of the string `str_x`. This ensures that if `shift` is greater than the length of `str_x`, it wraps around to the beginning of the string, effectively reversing the string. The result is then returned as a string.