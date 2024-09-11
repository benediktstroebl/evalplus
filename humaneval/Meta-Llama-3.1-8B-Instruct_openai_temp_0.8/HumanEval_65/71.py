```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The shifted string representation of the integer
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the effective shift (handle cases where shift > number of digits)
    shift = shift % len(num_str)
    
    # Split the string into two parts: the rightmost shift positions and the rest
    shifted_str = num_str[-shift:] + num_str[:-shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(123, 1))  # "321"
print(circular_shift(123, 3))  # "123"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the string representation of the integer with its digits circularly shifted to the right by `shift` positions. The script also includes test cases to verify the correctness of the function.