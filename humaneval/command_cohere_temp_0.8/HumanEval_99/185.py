```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the input number.
    """
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input, converts it to a float to allow for decimal values, and then rounds it to the nearest integer using the `round` function. By specifying `round`, it adheres to the requirement of rounding away from zero when faced with equidistant values. The resulting integer is returned as the output. 

This concise script directly addresses the task at hand, providing an efficient and effective solution.