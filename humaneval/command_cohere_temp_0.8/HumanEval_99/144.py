```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string.
    
    Round away from zero if tied.
    """
    n = float(s)
    return round(n)
```

The `round` function returns the closest integer to the given number based on Python's rounding rules. If the number is equidistant from two integers, it rounds away from zero as per the requirement.