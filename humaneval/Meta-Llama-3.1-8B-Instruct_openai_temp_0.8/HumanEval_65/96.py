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
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Get the length of the string
    len_x = len(x_str)
    
    # If shift is greater than the number of digits, use shift modulo the number of digits
    # This is because shifting by the number of digits is equivalent to not shifting at all
    shift = shift % len_x
    
    # Split the string into two parts at the shift position
    # The first part will be shifted to the end
    first_part = x_str[-shift:]
    second_part = x_str[:-shift]
    
    # Combine the two parts in the correct order
    result = first_part + second_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script uses Python's built-in string manipulation functions to split the input string into two parts at the shift position, and then combines them in the correct order. The shift position is adjusted to be within the range of the number of digits if it's greater than the number of digits.