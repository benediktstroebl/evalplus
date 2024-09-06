```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the specified base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 4)
    Traceback (most recent call last):
      File "<stdin>", line 29, in <module>
    TypeError: 'int' object does not support item assignment
    """
    if base == 10:
        return str(x)
    return '{:0{}d}'.format(x, base)
```