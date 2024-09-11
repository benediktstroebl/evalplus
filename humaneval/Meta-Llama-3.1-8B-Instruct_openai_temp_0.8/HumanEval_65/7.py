```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to shift.
    shift (int): The number of positions to shift.
    
    Returns:
    str: The shifted string representation of x.
    """
    # Convert the integer to a string for easier manipulation
    x_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return x_str[::-1]
    
    # Split the string into two parts at the shift point
    first_part = x_str[:-effective_shift]
    second_part = x_str[-effective_shift:]
    
    # Return the shifted string
    return second_part + first_part


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21" 
print(circular_shift(12345, 1))  # "23451"
print(circular_shift(12345, 5))  # "54321"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, performs the circular shift, and returns the result as a string. The `effective_shift` calculation ensures that the shift is taken modulo the number of digits, so that a shift greater than the number of digits is equivalent to reversing the string. The test cases at the end demonstrate the function's behavior.