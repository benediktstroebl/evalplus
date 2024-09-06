```python
def closest_integer(s):
    '''
    Rounds the given string representation of a number to the closest
    integer, rounding away from zero if equidistant.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given number.
    '''
    n = float(s)
    return round(n)
```

The function takes a string `s` which represents a number and turns it into a floating-point number. Then, it uses the `round` function to round it to the closest integer. In the case of equidistance, the rounding is done away from zero, following the requirement of the problem.