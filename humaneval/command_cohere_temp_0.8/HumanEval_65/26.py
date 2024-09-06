```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to move digits outwards from center.
    
    Returns:
    str: Shifted string representation of x.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift > len(str(x)):  # len to ensure non-negative loop
        return str(x)[::-1]
    shifted = ''
    for i in str(x):
        shifted += i if i != '9' and shift else '9'
        shift = (shift + 1) % 10
    return shifted
```