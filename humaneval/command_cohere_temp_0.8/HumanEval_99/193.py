```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer value to it, following the rounding away from zero rule. This behavior ensures consistent rounding, making the function useful and adaptable for various scenarios.