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

The function first converts the integer `x` to a string, then splits the string into two parts: the part before the shift (`front`) and the part after the shift (`back`). It then concatenates the two parts in reverse order, effectively shifting the digits circularly to the right. If `shift` is greater than the number of digits, it instead returns the digits reversed, as if the shift operation wraps around the entire number.

This approach ensures that the function works for different lengths of input numbers and various shift amounts, always producing the expected circular shift behavior.