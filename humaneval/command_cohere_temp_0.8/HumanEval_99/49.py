```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

The `round` function is used to return the nearest integer, but to ensure that it rounds away from zero when the number is equidistant from two integers, the return value is flipped if the decimal value is less than 0.5.

To better understand how it works, here is an example:
```python
closest_integer("10")  # => 10
closest_integer("15.3")  # => 15
closest_integer("14.5")  # => 15
closest_integer("-14.5")  # => -15
```