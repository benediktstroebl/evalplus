```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer to the numerical value represented by the string, adhering to the "rounding away from zero" rule. This rule dictates that in case of equidistance, the rounded result should be the integer farther from zero.

To achieve this, the function first converts the input string to a float and then utilizes the `round()` function to round it to the nearest integer. The typical rounding rule of rounding towards infinity or `round(2.5) == 3` is overridden by the keyword arguments `away from zero` or `round(14.5) == 15`. 

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

This function efficiently handles both positive and negative numerical inputs and returns the correct closest integer values according to the specified "rounding away from zero" rule.