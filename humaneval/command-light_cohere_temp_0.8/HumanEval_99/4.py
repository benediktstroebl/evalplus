```python
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number and returns the closest integer to it.
    If the number is equidistant from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    rounded to nearest int
    >>> closest_integer("14.5")
    value is going to be the same for rounding.
    >>> closest_integer("-14.5")
    value is being going to be the same for rounding.
    >>> closest_integer("13.9")
    need to round up 14 and 9 to get the closest integer.
    '''
    return round(value, 0) if value.isnumeric() else float(value)
```
Do you require any other assistance with coding or help with other problems?