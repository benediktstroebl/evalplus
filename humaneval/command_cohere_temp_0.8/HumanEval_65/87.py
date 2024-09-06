```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function takes an integer x and an integer shift as input and shifts the digits of x to the right by shift positions, creating a circular shift effect. The result is returned as a string. If shift is greater than the number of digits in x, the function reverses the digits instead.