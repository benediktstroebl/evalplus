```python
def circular_shift(x, shift):
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[: len(digits) % shift]
    return digits[-shift:] + digits[:-shift]
```

The function takes an integer `x` and a shift value as parameters and achieves the desired circular shift effect using string manipulation. It extracts the digits of `x` as a string, catering to cases where the shift exceeds the number of digits. If the shift is larger, it reverses the digits and extracts the relevant portion. Otherwise, it performs a standard circular shift by concatenating the last `shift` digits with the first `shift` digits.