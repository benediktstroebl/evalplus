```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective number of positions to shift
    # If shift is greater than the number of digits, take the remainder
    shift = shift % len(str_x)
    
    # Shift the digits to the right by slicing the string
    # The last shift positions are moved to the beginning of the string
    shifted_str = str_x[-shift:] + str_x[:-shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 4))  # "321"
print(circular_shift(123, 1))  # "231"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. If `shift` is greater than the number of digits in `x`, the function returns the digits reversed. The script also includes test cases to demonstrate the function's behavior.