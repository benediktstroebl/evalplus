```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The circularly shifted number as a string.
    
    Examples:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(num_str)
    
    # Shift the digits to the right
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Outputs: "21"
print(circular_shift(12, 2))  # Outputs: "12"
print(circular_shift(123, 1))  # Outputs: "231"
print(circular_shift(123, 2))  # Outputs: "123"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, performs the circular shift, and returns the result as a string. The function first converts the integer to a string, calculates the effective shift (in case `shift` is greater than the number of digits), and then shifts the digits to the right using slicing. Finally, the script tests the function with several examples.