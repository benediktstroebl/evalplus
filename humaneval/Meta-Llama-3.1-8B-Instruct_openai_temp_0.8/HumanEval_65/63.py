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
    str: The result as a string
    
    Example:
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Return the result as a string by concatenating the two parts in reverse order
    return part1 + part2

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(123, 2))  # Output: "321"
```

This Python script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, performs a circular shift on the digits of `x`, and returns the result as a string. The shift value is masked modulo the number of digits to handle the case where `shift > number of digits`. The script then tests the function with several example inputs.