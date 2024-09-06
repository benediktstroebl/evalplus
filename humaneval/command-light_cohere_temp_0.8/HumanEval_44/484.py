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
    >>> change_base(10, 10)
    '101010101'
    >>> change_base(0, -1)
    '0'
    >>> change_base(0, 5)
    '000'
    >>> change_base('123', 'Q')
    '2342'
    """
    return str(x if base == 10 else int(x, base))
```