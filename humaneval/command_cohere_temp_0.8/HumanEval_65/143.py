```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    digits = x[::-1] if shift > len(x) else x[len(x) - shift:] + x[:len(x) - shift]
    return digits
```

This code shifts the digits of the integer `x` right by `shift` and returns the result as a string. If `shift` is greater than the number of digits, it returns the digits reversed.

The function effectively handles shifts of various sizes, reversing the digits only when necessary. This is achieved through the use of smart slicing techniques to manipulate the string representation of the number `x`.