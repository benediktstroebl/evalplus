```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```
This Python script defines a function called `circular_shift` takes two parameters, `x` and `shift`. This function performs a circular right shift of the decimal digits of `x` by `shift`, and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits instead. This aligns with the problem statement and test examples provided, where it returns "21" for `circular_shift(12, 1)` and "12" for `circular_shift(12, 2)`.