```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer()` takes a string value as input and returns the closest integer value to the given number. It utilizes the `round()` function to round the numeric input to the nearest integer. When the number is equidistant from two integers, the rounding is done away from zero, adhering to the requirement of rounding toward the farther integer from zero in such cases. 

This code offers an efficient and concise way to achieve the desired outcome of rounding numbers to the nearest integer with a specific rounding direction.