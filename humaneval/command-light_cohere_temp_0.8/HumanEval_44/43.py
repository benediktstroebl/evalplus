```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another.
    :param x: int or string, base: int
    :return: string
    """
    if isinstance(x, str):
        x = int(x)
    if isinstance(x, int) and base > 0 and base <= 36:
        return "{:0>b}".format(x, base)
    else:
        raise ValueError("Invalid base number")

def test_change_base():
    """Test case for change_base function"""
    assert change_base(8, 3) == '22'
    assert change_base("8", 3) == '22'
    assert change_base(7, 2) == '111'
    assert change_base(5, 4) == '32'
    assert change_base(35, 10) == '35'
    assert change_base(10, 15) == '100000000'
    assert change_base("1231", 17) == '1728'
    assert change_base(5, -2) == '100'
    assert change_base(3, 38) == '1681'
    assert change_base(34567890, 5) == '234567890'
```
The `change_base` function changes the base of a number to a desired base. The `test_change_base` function tests the `change_base` function with various inputs to ensure its correctness.