```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers: 10
    """

    >>> change_base(8, 3)  # -> '22'
    >>> change_base(8, 2)  # -> '1000'
    >>> change_base(7, 2)  # -> '111'
    """
    if base == 10:
        return str(x)
    else:
        return '{:0}'.format(x, base)
```