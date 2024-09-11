```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits

    Returns:
    str: The shifted integer as a string
    """
    # Convert the integer to a string to easily manipulate its digits
    num_str = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(num_str)
    
    # If the effective shift is 0, return the original number
    if effective_shift == 0:
        return num_str
    
    # Split the string into two parts: the part to be shifted to the end, and the part to be kept at the beginning
    part_to_end = num_str[-effective_shift:]
    part_to_keep = num_str[:-effective_shift]
    
    # Return the shifted string by concatenating the two parts in the reverse order
    return part_to_end + part_to_keep


# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```