```python
def change_base(x: int, base: int):
    """
    Convert a number to another base using given base.

    Parameters:
    x: int, required. Reasons to convert a string representation from a given base.
    base: int, required to be 10, or a valid decimal.
    Returns: string representation of the number in the new base.
    """
```
def test_change_base():
    base = 10
    x = 8
    expected = '22'
    result = change_base(x, base)
    assert result == expected

    base = 2
    x = 1000
    expected = '1000'
    result = change_base(x, base)
    assert result == expected

    base = 7
    x = 111
    expected = '111'
    result = change_base(x, base)
    assert result == expected

test_change_base()
```