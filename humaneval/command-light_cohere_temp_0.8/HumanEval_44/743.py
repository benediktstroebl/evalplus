```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers are smaller than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return format(x, base)
```