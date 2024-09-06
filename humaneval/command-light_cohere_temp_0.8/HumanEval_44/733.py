```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a different base.
    """
    number = x * base
    return number.format(number, base)
    """
    tests for the change_base function:
    assert change_base(42, 10) == '2400'
    assert change_base(42, 2) == '2400'
    assert change_base(17, 5) == '5905'
    assert change_base(34, 7) == '1247'
    assert change_base(8, 3) == '22'
    assert change_base(85, 4) == '2401'
    return "Success"
```