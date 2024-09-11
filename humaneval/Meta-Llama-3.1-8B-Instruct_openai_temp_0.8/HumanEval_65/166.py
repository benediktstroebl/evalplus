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
        str: The shifted integer as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Combine the two parts in the correct order (shifted to the right) and return
    return first_part + second_part

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```
This script defines the `circular_shift` function, which takes an integer `x` and an integer `shift` as input, and returns the shifted integer as a string. The function works by first converting the integer to a string, then splitting the string into two parts at the effective shift position. The two parts are combined in the correct order (shifted to the right) and returned as a string.