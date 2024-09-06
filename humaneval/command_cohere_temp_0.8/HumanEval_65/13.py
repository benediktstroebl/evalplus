```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function accepts an integer x and an integer shift as parameters, utilizing the latter to circularly shift the digits of the former and returns the modified integer as a string. 

For example, if x is 12 and shift is 1, the function will return "21". If x is 12 and shift is 2, the function will return "12".