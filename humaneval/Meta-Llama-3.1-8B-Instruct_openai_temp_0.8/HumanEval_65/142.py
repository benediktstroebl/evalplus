```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to perform the circular shift on.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The resulting string after the circular shift.
    """
    # Convert the integer to a string to easily manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(num_str)
    
    # Perform the circular shift
    if effective_shift == 0:
        result = num_str
    else:
        result = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. The function first converts the integer to a string, then calculates the effective shift by taking the modulus of the shift with the number of digits. It then performs the circular shift by slicing the string and concatenating the resulting parts. If the shift is 0, it simply returns the original string.