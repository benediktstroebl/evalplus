```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```

This code provides a solution to the problem statement by converting the integer `x` to a string (`s = str(x)`), then performs a circular shift of the digits of this string, to do so it takes the characters from the end of the string (`s[shift:]`) and appends them to the front of the string (`s[:shift]`), this constitutes the required circular shift, and in cases where the `shift` is greater than the length of the number, it returns the reversed string (`return s[::-1]`).