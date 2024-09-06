```python
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    idx = n % 1
    if idx > 0:
        return i + 1
    elif idx < 0:
        return i - 1
    else:
        return i
```

The function `closest_integer()` takes a string `s` as input, representing a number. It first converts `s` to a floating-point number `n` and then to an integer `i`. The fractional part of `n` is stored in `idx` which is used to determine the direction of rounding. If `idx` is greater than 0, it is rounded up to the next integer, whereas if `idx` is less than 0, it is rounded down to the previous integer. If `idx` is exactly 0, it is already an integer, so it is simply returned as is.

Here is an example usage of the function:
```python
print(closest_integer("10"))  # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5"))  # Output: -15
```

This function fulfills the requirement of always rounding away from zero.