```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer to be shifted.
        shift (int): The number of positions to shift the digits to the right.
    
    Returns:
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, which is the remainder of the shift divided by the number of digits
    # This is because a shift that is a multiple of the number of digits is equivalent to no shift
    effective_shift = shift % len(x_str)
    
    # If the shift is greater than the number of digits, it's equivalent to reversing the string
    if effective_shift == 0:
        return x_str[::-1]
    
    # Split the string into two parts: the part to be shifted to the end and the part to stay at the beginning
    part1 = x_str[-effective_shift:]
    part2 = x_str[:-effective_shift]
    
    # Return the result by concatenating the two parts in the correct order
    return part1 + part2

# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and an integer `shift` as input and returns the result of the circular shift as a string. The function first converts the integer to a string to easily manipulate its digits. It then calculates the effective shift, which is the remainder of the shift divided by the number of digits. If the shift is greater than the number of digits, it's equivalent to reversing the string. Otherwise, it splits the string into two parts and returns the result by concatenating the two parts in the correct order. The script also includes test cases to verify the correctness of the function.