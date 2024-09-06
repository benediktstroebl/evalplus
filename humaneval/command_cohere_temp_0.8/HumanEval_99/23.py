```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    return round(float(s), 0, -1)
```

The function `round` is utilized with the parameters `float(s)`, `0` for rounding away from zero, and `-1` to use the "ceil" mode, which rounds the closest integer away from zero in cases of equidistance. The `float(s)` conversion is necessary as the `round` function expects a floating-point number as its first parameter.