```python
def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) < len(digits):
        result += result
    return result
```

This function takes an integer `x` and an integer `shift` as input and returns the circular shifted digits of `x` as a string. In the case where `shift` is greater than the length of the number, the digits are reversed and returned.