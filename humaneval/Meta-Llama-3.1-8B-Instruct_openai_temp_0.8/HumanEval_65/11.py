```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access each digit
    str_x = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # The part that is shifted out is placed at the beginning of the result
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 4))  # "321"
print(circular_shift(1234, 10))  # "4321"
```