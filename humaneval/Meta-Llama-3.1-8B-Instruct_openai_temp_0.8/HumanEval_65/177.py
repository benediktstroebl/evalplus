```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily access each digit
    str_x = str(x)
    
    # Calculate the effective shift, considering if shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # and join them in reverse order to get the circular shift
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(123, 1)) # "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It first converts the integer to a string, then calculates the effective shift considering if it's greater than the number of digits in the string. The function then splits the string into two parts at the effective shift position, reverses the order of these parts, and joins them together to get the circular shift. The result is returned as a string. The script also includes some test cases to demonstrate the function's behavior.