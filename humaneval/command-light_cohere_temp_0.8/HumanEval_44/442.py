```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: int, Input number
    :param base: int, New base
    :return: string representation of x in base base
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input and base")
    if base == 10:
        return str(x)
    elif base == 2:
        return f"{x:02}".replace("0", "")
    else:
        return str(x).format(f"{0}{:03}"))

def test_change_base():
    """
    Unit tests for change_base function
    """
    base = 10
    x = 8
    result = change_base(x, base)
    assert result == "22"
    base = 2
    x = 8
    result = change_base(x, base)
    assert result == "00008"
    base = 16
    x = -5
    with pytest.raises(ValueError("Invalid input and base")):
        result = change_base(x, base)
    assert result is None
    base = 2
    x = "abc"
    result = change_base(x, base)
    assert result == ""
    base = 32
    x = 3.14159
    base = 2
    result = change_base(x, base)
    assert result == "3.14159"

```
The `change_base` function accepts two arguments: a number `x` and a base `base`. It determines the new base representation of the input number `x` using the specified base. The `test_change_base` function conducts a set of unit tests to ensure that the `change_base` function operates correctly.