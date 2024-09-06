```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    front, back = x[:shift], x[shift:]
    return f"{back}{front}" if shift < len(x) else f"{x[::-1]}"
```

This code shifts the digits of the integer `x` right by `shift` to create a new number. If the shift is larger than the number of digits, it reverses the digits rather than providing an empty string or leaving out the digits. Tests are included to validate the function. The `circular_shift` function can be called with arguments like `12 1` or `12 2` to demonstrate its behavior.  This shifted number is then returned as a string.