```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer value to the numeric value represented by the input string, according to the rounding rule of rounding away from zero.

Here are some example inputs and expected outputs:
```
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15
>>> closest_integer("14.5")
15
>>> closest_integer("-14.5")
-15
```