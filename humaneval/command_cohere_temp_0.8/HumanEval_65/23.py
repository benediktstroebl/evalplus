```python
def circular_shift(x, shift):
    digits = str(x)
    if shift > len(digits):
        shift = shift % len(digits)
        return digits[len(digits) - shift:]+digits[:len(digits) - shift]
    return digits[shift:]+digits[:shift]
```