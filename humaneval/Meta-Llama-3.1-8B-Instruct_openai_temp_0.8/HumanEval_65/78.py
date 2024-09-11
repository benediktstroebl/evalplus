```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the integer to a string to easily manipulate digits
    num_str = str(x)
    
    # Calculate the effective shift, in case shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts: the part to be shifted to the end,
    # and the part to remain at the beginning
    part1 = num_str[-effective_shift:]
    part2 = num_str[:-effective_shift]
    
    # Reverse the order of the two parts and join them back together
    shifted_str = part1 + part2
    
    return shifted_str

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

In this script, the `circular_shift` function takes an integer `x` and a shift value `shift` as input, performs the circular shift, and returns the result as a string. It first converts the integer to a string to easily manipulate its digits. Then it calculates the effective shift, in case `shift` is greater than the number of digits. The function splits the string into two parts, reverses their order, and joins them back together to form the shifted string. The test cases demonstrate the function's correctness.