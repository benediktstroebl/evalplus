```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): Integer to shift digits of.
    shift (int): Number of positions to move the digit to the right.
    
    Returns:
    str: The shifted result as a string.
    """
    assert isinstance(x, int) and isinstance(shift, int)
    if shift == 0:
        return str(x)
    elif shift > 9:
        return circular_shift(int(str(x)[::-1]), shift - 10)
    else:
        result = []
        while x > 0:
            result.insert(0, str(x % 10))
            x //= 10
        result.insert(shift, result.pop())
        return ''.join(result)
```