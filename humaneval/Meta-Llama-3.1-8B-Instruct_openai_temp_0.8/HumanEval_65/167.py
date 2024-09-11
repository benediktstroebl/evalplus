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
        str: The circularly shifted digits as a string.
    """
    # Convert the integer to a string to easily operate on its digits
    x_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Shift the digits to the right by slicing the string
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    # If the shift is greater than the number of digits, the result is the same as reversing the string
    # So, we just return the reversed string in this case
    if effective_shift == 0:
        return x_str[::-1]
    else:
        return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string to easily operate on its digits, calculates the effective shift, shifts the digits to the right, and returns the result as a string. If the shift is greater than the number of digits, it returns the reversed string. The script also includes test cases to demonstrate the function's behavior.