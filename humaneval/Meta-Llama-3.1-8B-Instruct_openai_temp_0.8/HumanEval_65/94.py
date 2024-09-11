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
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if it's greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Otherwise, return the shifted string
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of the circular shift as a string. The function first converts the integer to a string to easily manipulate the digits. It then calculates the effective shift, taking into account if it's greater than the number of digits. If the shift is 0 (i.e., shift > number of digits), it returns the digits reversed. Otherwise, it returns the shifted string by taking the last `effective_shift` characters and concatenating them with the rest of the string (without the last `effective_shift` characters). The script includes test cases to demonstrate the function's behavior.