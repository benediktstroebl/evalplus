```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to move the digit to the right.

    Returns:
    str: Shifted integer as string.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift == 0:
        return str(x)
    elif shift < 0:
        return circular_shift(x, abs(shift))
    elif shift > len(str(x)):
        return circular_shift(x, len(str(x)) + shift % len(str(x)))
    else:
        dig_list = list(str(x))
        dig_list[:shift] = dig_list[-shift:]
        return ''.join(dig_list)
```