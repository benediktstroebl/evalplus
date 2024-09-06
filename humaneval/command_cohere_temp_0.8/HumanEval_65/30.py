```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    digits = x[:len(x) - x[::-1].index('0')] + x[len(x) - x[::-1].index('0') + shift:len(x)]
    return digits
```