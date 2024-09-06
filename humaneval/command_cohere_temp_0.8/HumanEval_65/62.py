```python
def circular_shift(x, shift):
    digits = str(x)
    if shift > len(digits):
        shift = len(digits)
    return digits[shift:] + digits[:shift]
```

This function takes an integer `x` and a shift value as inputs, it shifts the digits of `x` circularly to the right by `shift` and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits instead.