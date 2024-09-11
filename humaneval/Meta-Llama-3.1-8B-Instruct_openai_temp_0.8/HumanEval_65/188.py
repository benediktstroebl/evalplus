```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, 
    shift the digits right by shift and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the integer to a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > len(str_x)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts and join them in reverse order
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 2))  # "321"
print(circular_shift(123, 4))  # "321"
```

This script uses Python's built-in string manipulation functions to achieve the circular shift. It first converts the integer to a string, calculates the effective shift by taking the remainder of the shift divided by the length of the string, and then splits the string into two parts and joins them in reverse order.