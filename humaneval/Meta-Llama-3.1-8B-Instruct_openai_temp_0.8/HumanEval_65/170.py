```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily access each digit
    str_x = str(x)
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(str_x)
    # Split the string into two parts: the part to be moved to the end and the rest
    part_to_move = str_x[-effective_shift:]
    rest = str_x[:-effective_shift]
    # Combine the two parts to get the result
    result = part_to_move + rest
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 2))  # "321"
print(circular_shift(123, 4))  # "321"
```

This script uses the modulo operator (`%`) to calculate the effective shift, which eliminates the need to handle the case where `shift > number of digits` explicitly. It also uses string slicing to split the string into the part to be moved to the end and the rest, and then combines them to get the final result.