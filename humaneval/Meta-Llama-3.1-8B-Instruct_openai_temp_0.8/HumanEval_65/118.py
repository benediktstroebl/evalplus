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
        str: The result as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Otherwise, return the result of the circular shift
    return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and the number of positions to shift the digits `shift` as arguments. It converts the integer to a string to easily manipulate the digits. The effective shift is calculated as the remainder of `shift` divided by the number of digits. If this effective shift is 0, it means the shift is equal to the number of digits, so the function returns the digits reversed. Otherwise, it returns the result of the circular shift, which is the last `effective_shift` characters of the string followed by the rest of the string. The test cases are included at the end of the script to demonstrate the function's behavior.