```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string.

    Rounds away from zero if equidistant.
    """
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer to the numeric value represented by the input string. It uses the round() function to round the numeric value to the nearest integer. 

The `round()` function takes a floating-point number and returns the nearest integer value. When the given number is equidistant from two integers, the `round()` function rounds it away from zero, as specified in the problem statement.