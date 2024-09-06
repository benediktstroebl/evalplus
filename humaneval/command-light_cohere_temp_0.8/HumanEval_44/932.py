```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base.
    If string representation after the class() conversion.
    base numbers must be 10 or
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base == 10:
        return str(x)
    return format(x, str(base))
```