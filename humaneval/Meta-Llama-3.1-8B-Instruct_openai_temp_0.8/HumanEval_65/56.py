```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to shift.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access and manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, considering the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        effective_shift = len(x_str)
    
    # Perform the circular shift by slicing the string
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts `x` to a string, calculates the effective shift (considering the number of digits), and performs the circular shift by slicing the string. The result is returned as a string. The script also includes test cases to demonstrate the function's behavior.