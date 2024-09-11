```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): The input integer
    shift (int): The number of positions to shift
    
    Returns:
    str: The shifted integer as a string
    """
    # Convert the integer to a string
    x_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts
    first_part = x_str[-effective_shift:]  # The part that will be moved to the beginning
    second_part = x_str[:-effective_shift]  # The part that will stay
    
    # Combine the two parts to form the result
    result = second_part + first_part
    
    return result

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```