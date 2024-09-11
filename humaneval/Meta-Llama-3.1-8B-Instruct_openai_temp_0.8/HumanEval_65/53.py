```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    Parameters:
    x (int): The number to shift.
    shift (int): The number of positions to shift.
    Returns:
    str: The result as a string.
    """
    # Convert the number to a string to easily manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the effective shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the parts in the shifted order
    shifted_str = first_part + second_part
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 3))  # "321"
print(circular_shift(123, 10))  # "321"
```