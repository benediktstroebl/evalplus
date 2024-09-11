```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to shift.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily access each digit
    x_str = str(x)
    
    # Calculate the effective shift, in case shift is greater than the number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be moved to the end and the part to stay at the beginning
    part_to_move = x_str[-effective_shift:]
    part_to_stay = x_str[:-effective_shift]
    
    # Combine the two parts in the correct order to get the shifted string
    shifted_string = part_to_move + part_to_stay
    
    return shifted_string

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```