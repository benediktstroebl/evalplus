```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    return round(float(s), 0, -1)
```

The test cases include:
- Test case where `value` is already an integer, e.g.: `closest_integer("10")` should return `10`
- Test case where `value` is a decimal number, e.g.: `closest_integer("15.3")` should return `15`
- Test case where `value` is a decimal number rounded away from zero, e.g.: `closest_integer("14.5")` should return `15`
- Test case where `value` is a decimal number rounded away from zero (negative case), e.g.: `closest_integer("-14.5")` should return `-15`