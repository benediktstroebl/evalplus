```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted.
    shift (int): The number of positions to shift.
    
    Returns:
    str: The shifted number as a string.
    """
    # Convert the number to a string to easily extract and shift the digits
    num_str = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Shift the digits to the right
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift amount `shift` as input. It converts the number to a string, calculates the effective shift, and then shifts the digits to the right by concatenating the last `effective_shift` characters with the rest of the string. The result is returned as a string. The script also includes some test cases to verify the function's correctness.