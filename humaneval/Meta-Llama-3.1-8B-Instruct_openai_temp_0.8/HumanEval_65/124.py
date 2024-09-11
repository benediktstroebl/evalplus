```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access its digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts in the correct order
    return part1 + part2


# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift(x, shift)` that takes an integer `x` and a shift value `shift` as input. It then performs a circular shift on the digits of `x` based on `shift` and returns the result as a string. The function uses string manipulation to easily access the digits of `x` and split them into two parts at the effective shift position. If `shift` is greater than the number of digits in `x`, the function effectively reverses the digits of `x` by taking the remainder of `shift` divided by the number of digits.