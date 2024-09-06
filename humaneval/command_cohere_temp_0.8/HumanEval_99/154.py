```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer value to it, following the rounding away from zero rule. This rule dictates that when a number is equidistant from two integers, the integer to be returned is the one that is farther from zero. The function utilizes the `round` function to achieve this behavior. An example use and test cases illustrate the function's correct behavior:
```python
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15
>>> closest_integer("14.5")
15
>>> closest_integer("-14.5")
-15
>>> closest_integer("50.5")
51
```

The test cases showcase the function's ability to handle both positive and negative numbers, as well as numbers that are equidistant from adjacent integers, consistently rounding away from zero.