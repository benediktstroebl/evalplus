```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    Base numbers are less than 10, or return error.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    TraceError: cannot convert int to str (base 2)
    >>> change_base(7, 2)
    TraceError: cannot convert int to str (base 2)
    """
    return '{:0{}b}'.format(x, base)
```