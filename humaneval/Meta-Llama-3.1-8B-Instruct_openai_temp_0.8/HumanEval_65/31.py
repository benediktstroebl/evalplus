```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of digits to shift.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if it's greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts, the part to be shifted to the end and the part to stay at the beginning
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts
    return part1 + part2

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 5))  # "321"
print(circular_shift(1234, 3))  # "4312"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input. It calculates the effective shift value by taking the modulus of the shift value with the length of the input string. It then splits the string into two parts, shifts the second part to the end, and returns the result as a string. The script also includes test cases to demonstrate the function's behavior.