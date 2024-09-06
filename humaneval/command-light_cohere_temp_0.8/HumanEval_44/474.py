```python
def change_base(x: int, base: int) -> str:
    """
    Convert number to base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    return format(x, f', '.{{}{}'[base]).format(base, ''))
```