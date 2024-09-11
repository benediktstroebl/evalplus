```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result of the circular shift operation as a string.
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    shift = shift % len(str_x)  # handle shift > number of digits
    return str_x[-shift:] + str_x[:-shift]

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```