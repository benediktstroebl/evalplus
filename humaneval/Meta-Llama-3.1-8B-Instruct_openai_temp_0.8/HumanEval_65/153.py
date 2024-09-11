```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to perform the circular shift on.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the number to a string
    num_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(num_str)
    
    # Perform the circular shift
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, performs a circular shift on the digits of `x`, and returns the result as a string. The function handles cases where the shift amount is greater than the number of digits in `x` by calculating the effective shift as the remainder of the shift amount divided by the number of digits. The script also includes test cases to demonstrate the function's behavior.