```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Combine the two parts to form the result
    result = part1 + part2
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a `circular_shift` function that takes an integer `x` and a shift `shift` as input, and returns the result of the circular shift as a string. The function first converts the integer to a string, then calculates the effective shift (in case the shift is greater than the number of digits), splits the string into two parts based on the effective shift, and finally combines the two parts to form the result. The script also includes test cases to demonstrate the function's behavior.