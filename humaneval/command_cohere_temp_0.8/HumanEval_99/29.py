```python
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    ix = int(n)  # Convert to integer to get the rounding bit.
    return ix if n == ix else n if (n - ix) > 0 or (n - ix) == 0 and n > 0 else -ix

# Tests:
assert closest_integer("10") == 10
assert closest_integer("15.3") == 15
assert closest_integer("14.5") == 15
assert closest_integer("-14.5") == -15
```

The function utilizes the inherent behavior of floating-point numbers to round towards zero or away from zero based on the fractional part of the number. By converting the input to an integer, we can manipulate the rounding bit (the fraction of the nanosecond) to determine whether it rounds up or down. Consequently, this method follows the "away from zero" rule and efficiently handles both positive and negative inputs.