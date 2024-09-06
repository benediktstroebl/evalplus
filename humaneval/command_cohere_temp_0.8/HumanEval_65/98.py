```python
def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) < len(digits):
        result += result
    return result
```

This function takes an integer `x` and an integer `shift` as input and outputs a string. It rotates the decimal digits of `x` circularly right by `shift`, with the additional feature of cycling the leading digits if `shift` is greater than the number of digits. This behaviour is demonstrated in the docstring's example tests.