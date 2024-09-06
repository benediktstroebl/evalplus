```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    digits = len(x)
    if shift > digits:
        shift = shift % digits
    return x[-shift:] + x[:-shift]
```

This code provides a solution to the problem by taking an integer `x` and a shift value as inputs, shifting the digits of `x` circularly to the right by `shift` and returning the result as a string. For larger shift values compared to the number of digits, the code provides a reversed digit version of `x`.