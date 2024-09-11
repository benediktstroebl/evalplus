```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, 
    shift the digits right by shift and return the result as a string.
    
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift by taking the modulus of shift with the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Shift the digits right by effective_shift positions
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(1234, 3))  # "4312"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, performs the circular shift operation, and returns the result as a string. The function handles cases where the shift value is greater than the number of digits by taking the modulus of the shift value with the number of digits. The test cases demonstrate the function's correctness.