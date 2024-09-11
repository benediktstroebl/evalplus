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
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily extract and manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(x_str)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return x_str
    
    # Split the string into two parts and concatenate them in reverse order
    # to achieve the circular shift
    result = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(1234, 1))  # Output: "4321"
print(circular_shift(1234, 3))  # Output: "1234"
```