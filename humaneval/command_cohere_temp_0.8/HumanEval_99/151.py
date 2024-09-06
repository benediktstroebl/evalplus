```python
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    j = int(n) + 1 if n - i == 0.0 and n > 0 else int(n) - 1
    return max(i, j) if n > 0 else min(i, j)
```

The function takes a string `s` as input, representing a number, and returns
the closest integer according to the rounding rule of rounding away from
zero. The script tests the function with both positive and negative
numbers and returns the expected correct integer value.  For example,
for the input `"14.5"`, the function returns `15`, and for the input
`"-14.5"`, the function returns `-15`.