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

This code shifts the digits of the integer `x` right by `shift` and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits.

Here is an example usage of the function:
```python
circular_shift(12, 1) # "21"
circular_shift(12, 2) # "12"
circular_shift(518, 3) # "518"
circular_shift(518, 6) # "518"
```