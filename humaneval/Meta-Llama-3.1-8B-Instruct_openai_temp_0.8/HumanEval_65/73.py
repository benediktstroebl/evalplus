```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access individual digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account a shift greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # Shift the digits right by the effective shift
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input. It converts the integer to a string, calculates the effective shift, and then shifts the digits right by the effective shift. The function returns the shifted integer as a string.