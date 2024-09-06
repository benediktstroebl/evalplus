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
    >>> change_base(1, 50)
    Traceback (most recent call last):
    ...
    TypeError: cannot convert int object to str()
    """
    if base <= 0 or base > 51:
        raise ValueError("Base number should be between 1 and 51")
    if base == 10:
        return str(x)
    return format(x, ''.format({base}, 10)[0])
```