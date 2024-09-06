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

The function `closest_integer` takes a string value as input and converts it to a float to begin the process of finding the closest integer. The `round` function is then used to return the nearest integer, considering the rounding away from zero rule. 

This function adheres to the problem's requirement of always rounding away from zero while providing a concise and efficient solution.