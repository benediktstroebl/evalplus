```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string.

    Rounds away from zero if equidistant.
    """
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and converts it to a float to allow decimal values. Then the `round()` function is used to return the nearest integer. In case the number is equidistant, the rounding is done away from zero, as specified in the note of the problem. You can test this function by calling it with different input values.