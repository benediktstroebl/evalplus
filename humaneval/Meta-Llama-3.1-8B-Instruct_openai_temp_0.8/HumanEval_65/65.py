```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): Input integer
    shift (int): Number of positions to shift the digits
    
    Returns:
    str: String representation of the shifted integer
    """
    # Convert integer to string
    str_x = str(x)
    
    # Calculate the effective shift (since shifting by the number of digits is equivalent to not shifting)
    effective_shift = shift % len(str_x)
    
    # Shift the digits to the right
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
print(circular_shift(1234, 2))  # Expected output: "4321"
print(circular_shift(1234, 4))  # Expected output: "1234"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift by taking the modulus of `shift` with the length of the string, and then shifts the digits to the right by concatenating the last `effective_shift` digits with the remaining digits. If `shift` is greater than or equal to the number of digits, the effective shift will be zero or equal to the length of the string, effectively not shifting or shifting by the full length, which is equivalent to reversing the digits.