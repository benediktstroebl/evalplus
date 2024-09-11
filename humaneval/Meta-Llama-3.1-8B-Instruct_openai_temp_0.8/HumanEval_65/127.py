```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits to the right.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift, which is shift modulo the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return the digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Split the string into two parts at the effective shift position
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Combine the two parts to get the result
    result = part1 + part2
    
    return result

print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, and returns the result of shifting the digits of `x` to the right by `shift` positions as a string. If `shift` is greater than the number of digits in `x`, the function returns the digits in reverse order. The script also includes example use cases to demonstrate the function's behavior.