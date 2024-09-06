```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function accepts an integer `x` and an integer `shift` as input, and employs the `str` type to convert `x` to a string for easier manipulation. It then returns the last `shift` digits of the number first and then follows it with the first `shift` digits, effectively shifting the number circularly. This behavior is illustrated in the docstring's examples, where the shift is 1 and 2 respectively, showing the shifted digits.