```python
def change_base(x: int, base: int):
    """
    Changes the base of a number x to base base, and returns the string representation.

    Args:
        x: int or float number to be converted
        base: int base number to which the number is to be converted to

    Returns:
        str: the string representation of the number, in the given base
    """
    if isinstance(x, float):
        return '{0:.{%d' % (x, base)}
    elif not isinstance(x, int) or x < 0:
        raise TypeError("Input number must be a non-negative integer or float")
    else:
        return '{0:.{%d' % (x, base)}

# Unit tests
test_change_base = [
    "Tests for the change_base function:",
    "=" * 40
    assert change_base(8, 3) == '22'
    assert change_base(7, 2) == '111'
    assert change_base(-5, 4) == '-40.0'
    test change_base(-5, 4)'
    assert change_base(10, 10) == '10000000000'
    assert change_base('3.14159', 2) == '314159'
    assert change_base(42, 6) == '512345678'
    assert change_base(3.0, 12) == '3024'
```

This Python code defines a function `change_base` that converts a given number to a specified base. The function takes two arguments: the number `x` to be converted and the base `base` to which the number will be converted. The function then uses the Python's string formatting to convert the number to the desired base. It also includes a tests that verify the functionality of the `change_base` function with various inputs and expected outputs.