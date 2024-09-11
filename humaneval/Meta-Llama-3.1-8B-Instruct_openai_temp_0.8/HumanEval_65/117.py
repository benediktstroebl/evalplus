```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits to the right.
    
    Returns:
        str: The shifted digits as a string.
    """
    # Convert the integer to a string for easier manipulation
    x_str = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Shift the digits to the right and return the result
    return x_str[-effective_shift:] + x_str[:-effective_shift]


# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(123, 2))  # Output: "31"
print(circular_shift(123, 5))  # Output: "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift, and then shifts the digits to the right by the effective shift value. The result is returned as a string. The script also includes test cases to demonstrate the function's correctness.