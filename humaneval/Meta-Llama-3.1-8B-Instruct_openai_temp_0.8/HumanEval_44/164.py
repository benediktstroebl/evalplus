```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to convert.
    base (int): The target base.

    Returns:
    str: The string representation of the converted number.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


if __name__ == "__main__":
    # Test cases
    assert change_base(8, 3) == '22'
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    print("All test cases passed.")
```

This Python script defines a recursive function `change_base` that converts a given integer `x` from base 10 to a custom base `base`. The function uses integer division and modulo operations to recursively divide the input number by the base, appending the remainder to the result string. If the input number is less than the base, it returns the number as a string.

The test cases at the end of the script verify that the function works correctly for the provided examples.