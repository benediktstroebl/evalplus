```python
def circular_shift(x, shift):
    num_digits = len(str(x))
    x = str(x)
    if shift > num_digits:
        shift = num_digits
    return x[shift:] + x[:shift]
```

This script defines a function `circular_shift` that takes two arguments: `x`, which is the integer to be shifted, and `shift`, which specifies the number of places to shift the digits. The function shifts the digits of `x` to the right by `shift` positions and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits instead.

To achieve this, the function first determines the number of digits in `x` by taking the length of its string representation. It then converts `x` to a string, which allows us to easily manipulate individual digits. The digit shifting is done using string slicing, and the result is returned as a string.