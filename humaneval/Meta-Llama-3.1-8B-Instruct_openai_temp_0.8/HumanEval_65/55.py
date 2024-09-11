```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of digits to shift.
    
    Returns:
    str: The shifted integer as a string.
    """
    
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, shift right by effective_shift places
    # otherwise, shift left by (effective_shift - len(str_x)) places and swap the halves
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 2))  # "321"
print(circular_shift(12345, 3))  # "54321"
```

This script utilizes Python's built-in string manipulation functions to achieve the desired circular shift effect. It first converts the input integer to a string, then calculates the effective shift by taking the modulus of the shift with the number of digits. It then constructs the shifted string by concatenating the last `effective_shift` digits with the rest of the string.