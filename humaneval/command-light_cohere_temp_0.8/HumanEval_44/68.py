```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the base specified.
    Args:
        x: int, number to be changed
        base: int, base to be used
    Returns:
        str: representation of the number in the specified base
    """
    assert isinstance(x, int)
    assert isinstance(base, int)
    assert base >= 2
    assert x <= 10 ** base
    result = '{0:0' + base - 1}'.format(x)
    return result
```