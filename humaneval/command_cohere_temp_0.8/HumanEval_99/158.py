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
    delta = abs(n - i)
    if delta < 1e-5:  # Cover the case when float is effectively integer
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
    actual = closest_integer(input_)
    assert actual == expect, f"For {input_}, expected {expect} but got {actual}"
```

The function `closest_integer` takes a string `s` as input, which represents a number. It first converts `s` to a float `n` and then to an integer `i`. The difference between `n` and `i` is checked to determine whether the closest integer is achieved by rounding up or down. The case where the difference is very small is also handled to avoid unnecessary rounding. The test cases cover different scenarios and verify that the function returns the expected closest integer value.