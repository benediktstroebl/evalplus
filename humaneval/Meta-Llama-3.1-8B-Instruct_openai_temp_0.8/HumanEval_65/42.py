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
    x_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return x_str
    else:
        # Split the string into two parts: the last 'effective_shift' characters
        # and the rest of the string.
        last_shift_chars = x_str[-effective_shift:]
        rest = x_str[:-effective_shift]
        
        # Return the result of shifting the digits right by concatenating the
        # two parts in reverse order.
        return last_shift_chars + rest

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```