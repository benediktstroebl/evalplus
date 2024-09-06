Here is a Python script that contains a self-contained function that solves the problem along with its corresponding tests:
```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to the specified base.
    Args:
        x: number to be converted
        base: target base for conversion
    Returns:
        str: converted number
    """
    assert isinstance(x, int), "Input must be an integer"
    assert isinstance(base, int), "Base must be an integer"
    assert base > 0, "Base number must be greater than 0"

    if base == 10:
        return str(x)
    elif base == 2:
        return str(x).rstrip("0")
    elif base == 12:
        return str(x) + " " + str(x)[-2]
    else:
        return str(x)[len(str(x)) - base + "0"

def test_change_base():
    """
    Test cases for change_base function
    """
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(42, 10) == '40'
    assert change_base(42, 2) == '820'
    assert change_base(-123, 10) == '-1200'
    assert change_base(-123, 2) == '-600'
    assert change_base(123.0, 10) == '1400'
    assert change_base(123.0, 2) == '2320'
```

This Python code defines a function `change_base` that converts a number to a specified base. It includes a test cases for the `change_base` function to ensure its correctness, which are designed to pass the tests with `assert_change_base` function.