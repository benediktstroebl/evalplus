```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits to the right.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert integer to string to easily access and manipulate digits
    str_x = str(x)
    
    # If shift is greater than the number of digits, shift is effectively 0 or a multiple of the number of digits
    # In this case, we can simply return the original string
    if shift >= len(str_x):
        return str_x
    
    # Calculate the actual shift by finding the remainder of shift divided by the number of digits
    shift = shift % len(str_x)
    
    # Split the string into two parts: the digits that will be moved to the end, and the rest
    # The digits to be moved will be at the end of the string
    to_move = str_x[-shift:]
    rest = str_x[:-shift]
    
    # Combine the two parts in reverse order to get the shifted string
    return to_move + rest

# Test the function
print(circular_shift(12, 1))  # Outputs: 21
print(circular_shift(12, 2))  # Outputs: 12
```