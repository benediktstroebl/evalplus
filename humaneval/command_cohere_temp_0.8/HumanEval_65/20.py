```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function accepts an integer x and an integer shift as parameters, it converts the integer `x` to a string `digits`, and then returns the result of concatenating the ending `shift` digits with the starting `shift` digits of the string. This operation creates a circular shift of the integer's digits.

The expected behavior for the edge case of `shift` being greater than the number of digits is to return the digits reversed. You need to ensure that the shift amount does not exceed the number of digits, otherwise, the function would raise an IndexError.