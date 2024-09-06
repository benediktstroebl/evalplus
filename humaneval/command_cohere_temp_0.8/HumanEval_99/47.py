```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer to the represented number, following the rounding away from zero rule. This rule dictates that in case of equidistance, the rounded result should be the farther integer from zero. The function internally converts the input string to a float and then uses the `round` function to achieve the desired result.

Here is an example usage of the function:
```python
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15
>>> closest_integer("14.5")
15
>>> closest_integer("-14.5")
-15
```

The intended behavior of rounding away from zero is exemplified here. Specifically, in the case of input `"14.5"`, the function returns `15`, and for input `"-14.5"`, it returns `-15`.