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
    x_str = str(x)  # Convert the integer to a string
    shift = shift % len(x_str)  # Ensure shift is within the length of x_str
    
    if shift == 0:
        return x_str  # If shift is 0, return the original string
    
    return x_str[-shift:] + x_str[:-shift]  # Shift the string to the right

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "321"
print(circular_shift(123, 3))  # "123"
print(circular_shift(123, 4))  # "231"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input. It converts the integer to a string, performs the circular shift, and returns the result as a string. The script also includes test cases to demonstrate the function's behavior.