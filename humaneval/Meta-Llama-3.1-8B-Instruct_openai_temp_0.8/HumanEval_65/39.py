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
        str: The shifted integer as a string.
    """
    # Convert the integer to a string for easy manipulation
    str_x = str(x)
    
    # Find the number of digits in the string
    num_digits = len(str_x)
    
    # Calculate the effective shift, considering shifts greater than the number of digits
    effective_shift = shift % num_digits
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Combine the parts in reverse order to achieve the circular shift
    result = first_part + second_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```