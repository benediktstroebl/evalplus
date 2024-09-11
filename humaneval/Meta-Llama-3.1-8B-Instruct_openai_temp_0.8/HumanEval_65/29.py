```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be moved to the end
    # and the part to stay in its original position
    end_part = x_str[-effective_shift:]
    start_part = x_str[:-effective_shift]
    
    # Combine the two parts in reverse order
    result = end_part + start_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, applies a circular shift to the digits of `x`, and returns the result as a string. The effective shift is calculated as `shift % len(x_str)` to handle cases where `shift` is greater than the number of digits in `x`. The function splits the string representation of `x` into two parts, moves the first part to the end, and combines them in reverse order. The result is then returned as a string.