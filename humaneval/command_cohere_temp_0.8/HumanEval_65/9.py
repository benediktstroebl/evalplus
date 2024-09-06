```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function takes an integer `x` and an integer `shift` as input and circularly shifts the digits of `x` to the right by `shift`. If `shift` is greater than the number of digits, it reverses the digits.