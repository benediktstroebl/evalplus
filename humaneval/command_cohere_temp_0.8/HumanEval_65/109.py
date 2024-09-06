```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to move digits. Right moves is positive.
    
    Returns:
    str: Shifted integer as string.
    """
    assert isinstance(x, int) and isinstance(shift, int) and shift >= 0
    digits = str(x)
    if len(digits) <= shift:
        return digits[::-1]
    return digits[-shift:] + digits[:-shift]
```