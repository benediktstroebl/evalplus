```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift
    shift (int): Amount to shift by
    
    Returns:
    string: The shifted integer as a string
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift == 0:
        return str(x)
    elif shift < 0:
        return circular_shift(x, abs(shift))
    elif shift > len(str(x)):
        return circular_shift(x, len(str(x)) + shift % len(str(x)))
    else:
        num_str = str(x)
        return num_str[shift:] + num_str[:shift]
```