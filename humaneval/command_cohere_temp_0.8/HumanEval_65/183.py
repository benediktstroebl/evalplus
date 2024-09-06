```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```
This Python script defines a function called `circular_shift` which takes two parameters: `x`, which is supposed to be an integer, and `shift`, which is supposed to be an integer representing the amount by which to shift the digits of `x`. This function converts `x` to a string, and if the `shift` value is greater than the number of digits in `x`, it returns the reversed string. Otherwise, it shifts the digits circularly, and returns the shifted string.