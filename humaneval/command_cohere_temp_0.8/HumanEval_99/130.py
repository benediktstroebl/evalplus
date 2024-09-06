```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer to the numeric value represented by the string, adhering to the "rounding away from zero" rule. This rule dictates that in case of equidistance, the rounded result is selected to be the farther integer from zero. 

This code snippet provides a straightforward implementation of this rule in the function's behavior, achieving the desired result through the use of Python's built-in `round` function.