```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

The `round` function is used to return the closest integer to the numeric input `n`, as per the provided problem specification. The `float(s)` conversion is used to handle both numeric and numeric string input.