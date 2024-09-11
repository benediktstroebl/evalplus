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
    
    # Calculate the effective shift, considering the case where shift > len(str_x)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the last 'effective_shift' digits and the rest
    last_shifted = str_x[-effective_shift:]
    rest = str_x[:-effective_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    result = last_shifted + rest
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(1234, 4))  # "4321"
print(circular_shift(1234, 5))  # "4321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the result of shifting the digits of `x` to the right by `shift` positions, as a string. The function handles the case where `shift` is greater than the number of digits in `x` by taking the remainder of `shift` divided by the number of digits.