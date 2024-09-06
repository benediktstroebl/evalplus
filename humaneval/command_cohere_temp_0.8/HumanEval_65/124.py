```python
def circular_shift(x, shift):
    s = str(x)
    digits = len(s)
    if shift > digits:
        shift = shift % digits
    return s[-shift:] + s[:-shift]
```

This Python script defines a function called `circular_shift` takes two parameters, `x` and `shift`. This shifts the digits of the decimal number `x` right by `shift` and returns the result as a string. This is achieved by converting `x` to a string, finding the length of the decimal representation of `x` to determine the number of digits, and then using string slicing to perform the circular shift. If `shift` is greater than the number of digits, it performs a modulo operation to repeat the shift operation within the number's digits.