```python
def circular_shift(x, shift):
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[: len(digits) % shift]
    return digits[-shift:] + digits[:-shift]
```

This code provides a solution to the problem statement by handling the cases of shifts larger than the number of digits, and shifting either to the right or left, accordingly.