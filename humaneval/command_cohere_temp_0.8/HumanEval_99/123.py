```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string value to convert to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Remove trailing fractional part and convert to float
    val = float(s.rstrip('0123456789'))
    # Determine the closest integer and correct rounding direction
    return round(val, 0, -1 if val > 0 else 1)
```

The function `closest_integer` uses a few steps to ensure correct rounding:
1. It removes any trailing digits after the decimal point, ensuring the decimal point is removed only once.
2. The value is then converted to a float to make rounding easier.
3. The `round` function is used, but a special argument is passed to it: `round(val, 0, -1 if val > 0 else 1)`. This computes the usual rounding to the nearest integer, but the third argument (which is optional) dictates the direction of rounding. The value is rounded away from zero, ensuring the farthest integer from zero is chosen when tied.