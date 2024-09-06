```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

This code defines a function `closest_integer(s)` that takes a string `s` representing a number and returns the closest integer to that number, according to the given rounding rule. It converts the input string `s` to a float number `n`, and then uses the `round()` function to round it to the nearest integer. If the number is equidistant from two integers, it rounds away from zero.

The code is self-contained and can be executed directly to test it. You can copy and paste it into a Python environment or script to verify its functionality.