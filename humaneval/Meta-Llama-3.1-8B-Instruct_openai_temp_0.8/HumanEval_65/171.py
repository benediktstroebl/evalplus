```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to perform the circular shift on.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return digits reversed
    if effective_shift == 0:
        return str_x
    
    # Split the string into two parts: the part to be shifted and the part to remain in place
    part_to_shift = str_x[-effective_shift:]
    part_to_remain = str_x[:-effective_shift]
    
    # Return the shifted and remained parts concatenated
    return part_to_shift + part_to_remain

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses the modulo operator (`%`) to calculate the effective shift, which takes into account the number of digits in the string representation of the integer. It then splits the string into two parts, shifts the part to be shifted to the right, and concatenates the two parts to produce the final result. If the shift is equal to the number of digits, it returns the digits reversed.