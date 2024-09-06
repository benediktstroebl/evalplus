```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function accepts an integer `x` and an integer `shift` as inputs and utilises the `str` type to convert the former to a string for easier manipulation. It then returns the result of concatenating the second half of the digits (to the right of the centre) with the first half (to the left of the centre), achieving the desired circular shift effect.