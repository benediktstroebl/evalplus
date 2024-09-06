```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to shift circularly to the right.
    
    Returns:
    str: Shifted result as a string.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift == 0:
        return str(x)
    if shift < 0:
        x, shift = 13 - x, -shift  # flip x and shift, effectively reversing shift
    result = str(x)
    # shift digits right by abs(shift) positions, filling with leading digit
    circle_pos = result[0:1][::-1] * abs(shift)
    return circle_pos + result[shift:][::-1]
```