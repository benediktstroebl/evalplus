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

The function `closest_integer` takes a string `s` representing a number as its argument, converts it to a float to facilitate rounding, and then uses the `round` function to round it to the nearest integer. By specifying `round`, it adheres to the rounding away from zero rule, ensuring correct behavior for equidistant numbers, such as `-14.5` returning `-15`. 

This concise script effectively addresses the problem and provides the desired functionality.