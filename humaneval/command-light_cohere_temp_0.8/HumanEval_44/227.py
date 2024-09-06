```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(9, 10)
    '900'
    >>> change_base(10, 30)
    '3'
    >>> change_base(50, 5)
    '2'
    >>> change_base(123, 1)
    '123'
    """
    if base == 10:
        return str(x)
    if base == 2:
        return '{:0>2}'.format(x)
    return '{:0>{}}'.format(x, base)
```