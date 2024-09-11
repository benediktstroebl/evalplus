```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The resulting string after circular shift.
    """
    # Convert the integer to a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > len(str_x)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts: the part to be shifted to the end and the rest
    part_to_shift = str_x[-effective_shift:]
    rest = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts in the correct order
    return part_to_shift + rest

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```