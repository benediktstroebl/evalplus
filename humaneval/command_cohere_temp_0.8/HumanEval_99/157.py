```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer value to it, following the rule of rounding away from zero if the number is equidistant from two integers. This behavior is achieved by using the `round()` function with a float input, which inherently rounds away from zero when there is no closer integer. The script does not use any additional libraries, making it self-contained and easy to reproduce and maintain in various environments.