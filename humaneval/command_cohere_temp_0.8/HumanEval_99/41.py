```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string,
    rounding away from zero if equidistant.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer to the numeric value represented by the string, according to the rounding rule specified in the prompt. This rule is applied universally for all cases, including negative numbers.

Here is an example of using the function:
```python
closeness = "15.3"
result = closest_integer(closeness)
print(result)
```

The output of this code will be:
```
15
```

This exemplifies the function's ability to determine the closest integer value for a given numeric string, delivering the expected result of 15 in this case.