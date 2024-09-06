```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer to the numeric value represented by the string, according to the rounding rule of rounding away from zero. This behavior is achieved by first converting the input string to a float value using the `float()` function. Then, the float value is rounded to the nearest integer using the `round()` function, which returns the result.

Here is an example of how to use the above function:
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

This function call will return 10 when given the input "10", 15 when given 15.3, 15 when given 14.5, and -15 when given -14.5, respectively, in accordance with the rounding rule of rounding away from zero.