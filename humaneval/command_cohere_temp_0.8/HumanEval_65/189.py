```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift
    shift (int): Number of positions to shift by
    
    Returns:
    str: Shifted string representation of x
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift == 0:
        return str(x)
    elif shift >= len(str(x)):
        return x.__str__()[::-1]
    else:
        return str(x)[:len(str(x))-shift] + str(x)[-shift:]
```