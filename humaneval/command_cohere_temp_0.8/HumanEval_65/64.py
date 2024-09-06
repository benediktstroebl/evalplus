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

The function first converts the integer `x` to a string, then splits the string into two parts: the part before the shift and the part after the shift. If the shift is less than the length of the string, it concatenates the two parts and returns the result. If the shift is greater than the length of the string, it returns the digits reversed.

This approach solves the problem while maintaining a concise and readable Python script.