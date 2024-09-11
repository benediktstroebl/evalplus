### Circular Shift of Digits
#### Problem Description
Shift the digits of the integer `x` to the right by `shift` positions and return the result as a string. If `shift` is greater than the number of digits, reverse the digits.

#### Solution

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted integer as a string.
    """
    
    # Convert the integer to a string to easily access each digit
    str_x = str(x)
    
    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    effective_shift = shift % len(str_x)
    
    # If shift is greater than the number of digits, shift is equivalent to shifting all digits
    if effective_shift == 0:
        effective_shift = len(str_x)
        
    # Shift the digits to the right by slicing the string
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value as input and returns the shifted integer as a string. It first converts the integer to a string to easily access each digit. Then, it calculates the effective shift by finding the remainder of the shift divided by the number of digits. If the shift is greater than the number of digits, the effective shift is set to the number of digits. Finally, it shifts the digits to the right by slicing the string and returns the result.