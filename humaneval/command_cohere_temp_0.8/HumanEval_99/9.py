```python
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    delta = abs(n - i)
    if delta < 1e-5:  # Cover the case where the float is effectively an integer
        return i
    elif n > 0:
        return i + 1 if delta == 0.5 else i
    else:
        return i - 1 if delta == 0.5 else i

# Tests
cases = [
    ("10", 10),
    ("15.3", 15),
    ("14.5", 15),
    ("-14.5", -15),
    ("17.8", 18),
    ("-17.8", -18),
]

for input_, expect in cases:
    assert closest_integer(input_) == expect
```

The function `closest_integer` takes a string value as its argument and returns the closest integer value, rounding away from zero. It first converts the input value to a float and then to an integer. The difference between the original float and the integer is calculated (`delta`). If `delta` is less than a very small threshold (`1e-5`), it means the original value is already effectively an integer, so it returns the integer value as is. If `delta` is equal to 0.5, it means the number is equidistant from two integers, so it returns the one away from zero. Otherwise, it returns the integer value as is.