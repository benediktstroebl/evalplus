```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The shifted digits as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the actual shift, considering if it's greater than the number of digits
    actual_shift = shift % len(str_x)
    
    # Split the string into two parts at the actual shift position
    part1 = str_x[-actual_shift:]
    part2 = str_x[:-actual_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    shifted_str = part1 + part2
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Should print "21"
print(circular_shift(12, 2))  # Should print "12"
print(circular_shift(123, 2))  # Should print "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input, and returns the shifted digits as a string. The function first converts the integer to a string, calculates the actual shift considering if it's greater than the number of digits, splits the string into two parts at the actual shift position, and combines the two parts in reverse order to get the shifted string. The script also includes test cases to verify the correctness of the function.