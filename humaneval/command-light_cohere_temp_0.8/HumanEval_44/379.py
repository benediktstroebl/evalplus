```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another. string the number to a desired base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    return format(x, base)
```