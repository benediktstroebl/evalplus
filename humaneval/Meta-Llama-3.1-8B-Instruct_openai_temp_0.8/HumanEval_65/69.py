```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the number to a string to easily access and shift digits
    num_str = str(x)
    
    # Calculate the effective shift, considering if it's greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the effective shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts to get the shifted string
    shifted_str = first_part + second_part
    
    return shifted_str


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It converts the integer to a string, calculates the effective shift, splits the string into two parts at the effective shift position, and combines them to get the shifted string. Finally, it includes test cases to demonstrate the function's correctness.