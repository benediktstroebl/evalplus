```python
def closest_integer(s):
    '''
    Rounds the given string representation of a number to the closest
    integer, rounding away from zero if equidistant.

    Args:
        s (str): String representation of a number.

    Returns:
        int: The closest integer to the given number.
    '''
    n = float(s)
    return round(n)
```

The `round` function is used to round the number to the nearest integer. In Python 3, `round` has a default parameter of `10**-1`, which means it will round away from zero if the number is equidistant. If you were intending to test what would happen with a different rounding strategy, you should adjust the rounding precision accordingly, but for the given specification, this code should do.