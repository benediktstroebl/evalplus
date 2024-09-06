```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number to the specified base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    if base > x or base < 2 or base == 0:
        raise ValueError("Invalid base value.
    return format(x(x), base)
```