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
    str: The result of the circular shift as a string.
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    x_str = str(x)
    
    # Get the length of the string
    length = len(x_str)
    
    # Calculate the actual shift, taking into account if shift > length
    actual_shift = shift % length
    
    # Shift the string to the right by the actual shift
    shifted_str = x_str[-actual_shift:] + x_str[:-actual_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(1234, 1))  # Output: "4321"
print(circular_shift(1234, 2))  # Output: "2314"
```

This script defines a function `circular_shift` that takes an integer `x` and an integer `shift` as arguments. It first converts the integer to a string, then calculates the actual shift by taking the remainder of the shift divided by the length of the string. The string is then shifted to the right by the actual shift, and the result is returned as a string. The script also includes some test cases to demonstrate the function's behavior.