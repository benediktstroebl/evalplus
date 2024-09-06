```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    Args:
        x: int, number to be converted
        base: int, base to which the number will be converted.
    Returns: string representation of the number.
    """
    above, return the string representation of the number using the specified base.
    """
```
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(7, 5) == '31'
    assert change_base(-9, 2) == '-180'
    assert change_base(10, 5) == '55'
    assert change_base(3, 10) == '30'

```
This script defines a function `change_base` that converts a number to a new base. It also provides a test cases and asserts the results against the expected output.