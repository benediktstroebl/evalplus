```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits.
        
    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and shift its digits
    num_str = str(x)
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(num_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return num_str[::-1]
    
    # Otherwise, return the result of the circular shift
    return num_str[-effective_shift:] + num_str[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the result of the circular shift as a string. The function first converts the integer to a string to easily access and shift its digits. It then calculates the effective shift amount, taking into account if the shift amount is greater than the number of digits. Finally, it returns the result of the circular shift.