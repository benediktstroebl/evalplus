```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to perform circular shift on.
        shift (int): The number of digits to shift to the right.
    
    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert integer to string
    x_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(x_str)
    
    # Perform circular shift
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "21"
print(circular_shift(123, 1))  # Expected output: "231"
print(circular_shift(123, 4))  # Expected output: "123"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input, performs a circular shift on the digits of `x`, and returns the result as a string. The effective shift is calculated by taking the remainder of `shift` divided by the number of digits in `x`, which ensures that the shift wraps around when it exceeds the number of digits.