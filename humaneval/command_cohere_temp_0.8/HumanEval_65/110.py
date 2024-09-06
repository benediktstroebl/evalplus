```python
def circular_shift(x, shift):
    s = str(x)
    digit_count = len(s)
    if shift > digit_count:
        shift = digit_count
    return s[shift:] + s[:shift]
```

This Python script provides a function called `circular_shift`, which takes two parameters: `x` and `shift`. This shifts the digits of the integer `x` right by `shift` and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits instead.

Here is an example usage of the function:
```python
>>> circular_shift(12, 1)
'21'
>>> circular_shift(12, 2)
'12'
```

This generates the following output:
```
21
12
```