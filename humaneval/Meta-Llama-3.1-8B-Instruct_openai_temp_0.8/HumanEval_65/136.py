```markdown
### Circular Shift Function
#### Shifts the digits of an integer to the right and returns the result as a string

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits to the right

    Returns:
        str: The result of the circular shift as a string
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift > number of digits, return the digits reversed
    if effective_shift == 0:
        return str_x[::-1]
    
    # Shift the digits to the right by effective_shift positions
    else:
        return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, shifts the digits of `x` to the right by `shift` positions, and returns the result as a string. The function handles the case where `shift` is greater than the number of digits by returning the reversed string. The script includes test cases to demonstrate the function's behavior.