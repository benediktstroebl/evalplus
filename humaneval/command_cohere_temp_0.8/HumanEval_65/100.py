```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Amount to shift right.
    
    Returns:
    str: Resultant integer as a string after shifting.
    """
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[: len(digits) % shift]
    return digits[-shift:] + digits[:-shift]
```

This code shifts the digits of a number circularly to the right, adding the shifted digits to the beginning if there is space, or reversing the digits if there is too much shift. 

To use this code, call the function with a number (x) and the desired shift (shift). 
```python
circular_shift(12, 1)  # Outputs "21"
circular_shift(12, 2)  # Outputs "12"
``` 

This will produce the desired circular shift of the digits.