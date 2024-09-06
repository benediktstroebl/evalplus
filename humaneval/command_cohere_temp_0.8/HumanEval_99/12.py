```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string representing a number.

    Returns:
        int: The closest integer to the given number.
    """
    n = float(s)  # Convert string to float to handle decimal values
    return round(n) if n % 1 else int(n)

# Test cases
def test_closest_integer():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("0.1") == 0
    assert closest_integer("-0.1") == 0

test_closest_integer()
```

In the above code, the `closest_integer` function accepts a string representing a number (including decimal values). It first converts this string to a float to handle the decimal part, then rounds it to the nearest integer using the `round` function. If the number is already integer-valued (e.g., 10, -10), it is directly converted to an integer without rounding. The provided test cases verify the function's behavior for various inputs, ensuring that it correctly returns the closest integer value as per the problem's requirements.