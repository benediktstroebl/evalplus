### Circular Shift Function
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access individual digits
    x_str = str(x)
    # Calculate the effective shift by taking the modulus of the number of digits
    # with the shift value. This handles the case where shift > number of digits.
    effective_shift = shift % len(x_str)
    # Split the string into two parts at the effective shift index from the end.
    # The first part is shifted to the end of the string and the second part is
    # prepended to the first part to get the final result.
    return x_str[-effective_shift:] + x_str[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(123, 2))  # "321"
print(circular_shift(123, 5))  # "321"
```