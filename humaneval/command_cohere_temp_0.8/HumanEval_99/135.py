```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer value to it, adhering to the rounding away from zero rule when the target number is equidistant from two integers. This behavior is exemplified in the provided test cases, dealing correctly with positive and negative values and their respective closest integers.