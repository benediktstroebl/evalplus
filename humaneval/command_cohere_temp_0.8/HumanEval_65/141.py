```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to move digits shifted to.
    
    Returns:
    str: String of shifted digits.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift > 0:
        extra_shift = shift % len(str(x)) # this makes sure we loop around 
        reversed_str = str(x)[:len(str(x))-extra_shift:]
        reversed_str = reversed_str[::-1]
        result = str(x)[:len(str(x))-shift] + reversed_str
    elif shift == 0:
        result = str(x)
    else:
        result = str(x)[::-1]
    return result
```