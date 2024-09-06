```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Amount to shift circularly to the right.
    
    Returns:
    str: Resultant string after shifting digits.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift > 0:
        return '{0:0{1}b}'.format(x, shift).rjust(len(str(x)), '0')
    elif shift == 0:
        return str(x)
    else:
        return '{0:0{1}b}'.format(x, -shift).ljust(len(str(x)), '0')
```