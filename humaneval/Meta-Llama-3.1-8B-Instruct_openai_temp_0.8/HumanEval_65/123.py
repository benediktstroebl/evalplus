```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted string representation of the integer.
    
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Perform the circular shift
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift (in case the shift value is greater than the number of digits), performs the circular shift, and returns the result as a string. The test cases at the end demonstrate the function's behavior.