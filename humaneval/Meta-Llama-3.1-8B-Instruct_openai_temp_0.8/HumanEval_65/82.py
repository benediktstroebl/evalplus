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
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access individual digits
    x_str = str(x)
    
    # Calculate the effective number of positions to shift
    # This is done by finding the remainder of shift divided by the number of digits
    effective_shift = shift % len(x_str)
    
    # Perform the circular shift by slicing the string and concatenating the two parts
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "321"
print(circular_shift(123, 3))  # "123"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`. It converts `x` to a string, calculates the effective number of positions to shift, and then performs the circular shift by slicing the string and concatenating the two parts. The result is returned as a string. The script includes test cases to demonstrate the function's behavior.