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
        str: The circularly shifted string.
    """
    # Convert the integer to a string to easily operate on its digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(str_x)
    
    # If the shift is greater than the number of digits, reverse the string
    if effective_shift == 0:
        return str_x[::-1]
    
    # Shift the string to the right by the effective shift
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift value, and then shifts the string to the right by the effective shift value. If the shift value is greater than the number of digits in the string, it reverses the string. Finally, it returns the shifted string. The script includes test cases to verify the correctness of the function.