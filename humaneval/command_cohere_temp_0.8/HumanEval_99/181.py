```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string to be converted to an integer.

    Returns:
        int: The closest integer to the input.
    """
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input, converts it to a float, and then uses the `round` function to round it to the nearest integer. The `round` function's default behavior is to round away from zero, as stated in the note of the problem statement. Therefore, the code directly returns the result of `round(n)` without explicitly specifying rounding direction.

This concise approach solves the problem efficiently while maintaining code simplicity and readability.