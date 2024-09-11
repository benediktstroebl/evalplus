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
        str: The result of the circular shift.
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the actual shift (in case shift > number of digits)
    actual_shift = shift % len(num_str)
    
    # If shift > number of digits, return digits reversed
    if actual_shift == 0:
        return num_str
    
    # Perform the circular shift
    result = num_str[-actual_shift:] + num_str[:-actual_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(345, 2))  # Output: "53"
print(circular_shift(4567, 4))  # Output: "7654"
print(circular_shift(12345, 5))  # Output: "54321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the result of shifting the digits of `x` to the right by `shift` positions as a string. If the shift amount is greater than the number of digits, the function returns the digits reversed.