```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted
        shift (int): The number of positions to shift the digits to the right

    Returns:
        str: The shifted digits as a string
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)
    
    # Calculate the actual shift positions, considering cases where shift > len(str_x)
    actual_shift = shift % len(str_x)
    
    # Shift the digits to the right by the actual shift positions
    shifted_str_x = str_x[-actual_shift:] + str_x[:-actual_shift]
    
    return shifted_str_x

# Test cases
print(circular_shift(12, 1)) # Output: "21"
print(circular_shift(12, 2)) # Output: "12"
```