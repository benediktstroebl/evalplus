```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, 
    shift the digits right by shift and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The shifted number as a string.
    
    Example:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the number to a string to easily access individual digits
    num_str = str(x)
    
    # Calculate the effective shift, taking into account the number of digits
    effective_shift = shift % len(num_str)
    
    # If the shift is greater than the number of digits, return the digits reversed
    if effective_shift == 0:
        return num_str[::-1]
    
    # Split the number into two parts: the part to be shifted to the end, and the part to remain at the beginning
    part_to_end = num_str[-effective_shift:]
    part_to_beginning = num_str[:-effective_shift]
    
    # Return the result as a string
    return part_to_end + part_to_beginning

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This Python script defines the `circular_shift` function that takes an integer `x` and an integer `shift` as input. It then calculates the effective shift, splits the number into two parts, and returns the shifted number as a string. The script includes test cases to demonstrate its functionality.