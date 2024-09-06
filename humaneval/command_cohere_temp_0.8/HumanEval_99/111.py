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
    delta = 1.0

    if n - i == 0:
        return i

    if n > i:
        delta = -1.0
        i += 1
    elif n < i:
        i -= 1

    return int(i / delta)

# Testing code
def test_closest_integer():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("2.2") == 2

test_closest_integer()
```

In this script, the `closest_integer` function takes a string `s` representing a number as its argument and calculates the closest integer using the rules specified in the problem statement: if the number is equidistant from two integers, it rounds away from zero. The `test_closest_integer` function runs simple test cases and asserts the expected results. Finally, the test function is called to run the tests.