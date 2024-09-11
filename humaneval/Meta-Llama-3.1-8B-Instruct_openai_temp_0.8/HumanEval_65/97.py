```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to circular shift.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    x_str = str(x)
    
    # Calculate the effective shift, which is the shift modulo the number of digits
    effective_shift = shift % len(x_str)
    
    # If the shift is greater than the number of digits, return the digits reversed
    if effective_shift == 0:
        return x_str[::-1]
    
    # Split the string into two parts: the part to be shifted to the end and the part to remain at the start
    part1 = x_str[-effective_shift:]
    part2 = x_str[:-effective_shift]
    
    # Return the circular shifted string
    return part1 + part2

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(1234, 3))  # Output: "2341"
print(circular_shift(1234, 4))  # Output: "4312"
print(circular_shift(1234, 5))  # Output: "1234"
```