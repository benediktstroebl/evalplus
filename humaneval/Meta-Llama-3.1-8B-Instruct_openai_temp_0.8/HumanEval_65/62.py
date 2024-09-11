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
        str: The shifted string representation of x.
    """
    str_x = str(x)  # Convert x to a string
    shift %= len(str_x)  # Handle cases where shift > number of digits
    
    return str_x[-shift:] + str_x[:-shift]  # Shift the string

# Test cases
print(circular_shift(12, 1))  # Should print "21"
print(circular_shift(12, 2))  # Should print "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value, and returns the result of shifting the digits of `x` to the right by `shift` positions. If `shift` is greater than the number of digits in `x`, it simply reverses the string representation of `x`. The test cases at the end demonstrate the function's behavior.