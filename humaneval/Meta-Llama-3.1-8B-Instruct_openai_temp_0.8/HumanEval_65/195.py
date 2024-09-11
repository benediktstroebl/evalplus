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
        str: The resulting string after shifting the digits.
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, shift right is same as shift left, so return the reversed string
    if effective_shift == 0:
        return str_x[::-1]
    
    # Otherwise, shift the string to the right by effective_shift positions
    else:
        return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```