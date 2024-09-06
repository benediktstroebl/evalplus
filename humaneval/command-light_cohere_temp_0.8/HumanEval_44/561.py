```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    If string representation after conversion.
    base numbers are 10.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    return '{:0b}'.format(x, base)
```