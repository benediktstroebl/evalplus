```python
def closest_integer(s):
    '''
    Rounds the given string representation of a number to the closest
    integer, rounding away from zero if equidistant.

    Args:
        s (str): Number string to be rounded

    Returns:
        int: The closest integer to the input number
    '''
    n = float(s)
    i = int(n)
    d = n - i
    if d == 0:   # If the number is already an integer, return it as is
        return i
    elif d < 0:  # If the number is less than the closest integer
        return i - 1
    elif d > 0:  # If the number is greater than the closest integer
        return i + 1
    else:
        assert False, "Should not reach this line!"
```