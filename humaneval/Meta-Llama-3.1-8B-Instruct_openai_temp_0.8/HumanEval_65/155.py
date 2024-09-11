```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer whose digits need to be shifted.
        shift (int): The number of positions to shift the digits right.
        
    Returns:
        str: The result of circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate digits
    x_str = str(x)
    
    # Calculate the effective shift, in case it's greater than the number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the part to be shifted and the part to be prepended
    # The part to be shifted is from the effective shift position to the end
    # The part to be prepended is from the start to the effective shift position
    shifted_part = x_str[-effective_shift:]
    prepended_part = x_str[:-effective_shift]
    
    # Return the result by concatenating the two parts
    return shifted_part + prepended_part

# Test cases
print(circular_shift(12, 1)) # "21"
print(circular_shift(12, 2)) # "12"
print(circular_shift(1234, 2)) # "43"
```

This script first converts the integer `x` to a string, which allows us to easily access and manipulate its digits. It then calculates the effective shift, which is the remainder of the shift divided by the number of digits. This is because shifting by any multiple of the number of digits is equivalent to not shifting at all. 

It then splits the string into two parts: the part to be shifted and the part to be prepended. The part to be shifted is from the effective shift position to the end, and the part to be prepended is from the start to the effective shift position.

Finally, it returns the result by concatenating the two parts.