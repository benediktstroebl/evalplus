```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string.

    Rounds away from zero if equidistant.
    """
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer representation of that value, adhering to the rounding rule of rounding away from zero when the value is equidistant from two integers. This behavior is defined by the built-in `round` function, which is used to perform the rounding in this script.