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
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    # If shift is greater than the number of digits, reverse the string
    if effective_shift == 0:
        return str_x[::-1]
    # Otherwise, perform the circular shift by concatenating the last 'effective_shift' characters with the rest of the string
    else:
        return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```