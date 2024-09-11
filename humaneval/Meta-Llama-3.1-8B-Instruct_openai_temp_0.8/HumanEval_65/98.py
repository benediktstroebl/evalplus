```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of places to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Determine the actual shift, taking into account if shift is greater than the number of digits
    actual_shift = shift % len(str_x)
    
    # Perform the circular shift
    result = str_x[-actual_shift:] + str_x[:-actual_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string, then determines the actual shift by taking the modulus of the shift with the length of the string. This ensures that if the shift is greater than the number of digits, it is reduced to the equivalent shift within the number of digits. Finally, it performs the circular shift by concatenating the last `actual_shift` digits with the rest of the string (excluding the last `actual_shift` digits). The result is returned as a string. The script also includes test cases to verify the function's behavior.